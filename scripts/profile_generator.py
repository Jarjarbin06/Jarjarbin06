import os
import requests
from datetime import datetime

USERNAME: str = os.getenv("USERNAME")
IGNORED: list = os.getenv("GH_IGNORED_REPO").split(" ")
TOKEN: str = os.getenv("GH_TOKEN")

HEADERS = {
    "Authorization": f"token {TOKEN}"
}


# -----------------------------
# GitHub API helper
# -----------------------------
def gh_get(url):
    r = requests.get(url, headers=HEADERS)
    r.raise_for_status()
    return r.json()


# -----------------------------
# 1. PROJECT INDEX GENERATOR
# -----------------------------
def generate_projects(repos):
    categorized = {}
    language_map = {}
    
    def contained(str_name: str, list_names: list[str]):
        for name in list_names:
            if name in str_name:
                return True
        return False

    for repo in repos:
        name = repo["name"]
        url = repo["html_url"]
        lang = repo["language"] or "Unknown"
        updated = repo["updated_at"]
        
        if name in IGNORED:
            continue

        language_map[lang] = language_map.get(lang, 0) + 1

        category = "misc"
        if contained(name, ["lib"]):
            category = "libraries"
        elif contained(name, ["tool", "JCCS", "epitech_console"]):
            category = "tools"

        categorized.setdefault(category, []).append(
            f"- [{name}]({url}) (updated: {updated[:10]})"
        )

    out = "# 📦 Projects Index\n\n"

    for cat, items in categorized.items():
        out += f"## 🔹 {cat.title()}\n"
        out += "\n".join(items) + "\n\n"

    out += "## 🔹 Language Breakdown\n"
    for lang, count in language_map.items():
        out += f"- {lang}: {count}\n"

    return out


# -----------------------------
# 2. ACTIVITY BLOCK
# -----------------------------
def generate_activity(repos):
    sorted_repos = sorted(repos, key=lambda x: x["pushed_at"], reverse=True)

    out = "# 📡 Latest Activity\n\n"

    out += "## 🔹 Recent Updates\n"
    for repo in sorted_repos[:10]:
        out += f"- {repo['name']} → {repo['pushed_at'][:10]}\n"

    active = [r for r in repos if (datetime.utcnow() - datetime.strptime(r["pushed_at"], "%Y-%m-%dT%H:%M:%SZ")).days < 30]

    out += "\n## 🔹 Active Repositories (30 days)\n"
    for repo in active:
        out += f"- {repo['name']}\n"

    return out


# -----------------------------
# 3. VERSION TRACKING SYSTEM
# -----------------------------
def extract_version(repo):
    try:
        contents = gh_get(repo["url"] + "/contents")
        for file in contents:
            if "Makefile" in file["name"]:
                raw = requests.get(file["download_url"]).text
                for line in raw.splitlines():
                    if "VERSION" in line or "v" in line:
                        return line.strip()
    except:
        return "unknown"
    return "unknown"


def generate_versions(repos):
    out = "# 🧩 Version Tracking\n\n"

    tracked = ["JCCS", "Epitech", "libfile"]

    for repo in repos:
        for key in tracked:
            if key.lower() in repo["name"].lower():
                version = extract_version(repo)
                out += f"- **{repo['name']}** → {version}\n"

    return out

def replace_readme():
    with open("README_template.md", 'r') as file:
        readme = file.read()

    print(f"template opened")

    with open("generated/projects.md", 'r') as file:
        projects = file.read()

    readme = readme.replace(
        "<!-- GENERATED:PROJECTS -->",
        projects
    )

    print(f"projects filled in template")

    with open("generated/activity.md", 'r') as file:
        activity = file.read()

    readme = readme.replace(
        "<!-- GENERATED:ACTIVITY -->",
        activity
    )

    print(f"activity filled in template")

    with open("generated/versions.md", 'r') as file:
        versions = file.read()

    readme = readme.replace(
        "<!-- GENERATED:VERSIONS -->",
        versions
    )

    print(f"versions filled in template")

    with open("README.md", 'w') as file:
        file.write(readme)

    print(f"template copied to final")


# -----------------------------
# MAIN
# -----------------------------
def main():
    if is_test:
        print(f"{is_test=} {USERNAME=} {TOKEN=}")
    
    print(f"""
username found ? {bool(USERNAME)}
token found ? {bool(TOKEN)}
""")

    repos = gh_get(f"https://api.github.com/users/{USERNAME}/repos?per_page=100")

    print(f"""
repos count ? {len(repos)}
""")

    os.makedirs("generated", exist_ok=True)

    with open("generated/projects.md", "w") as f:
        f.write(generate_projects(repos))

    print(f"projects.md generated")

    with open("generated/activity.md", "w") as f:
        f.write(generate_activity(repos))

    print(f"activity.md generated")

    with open("generated/versions.md", "w") as f:
        f.write(generate_versions(repos))
    
    print(f"versions.md generated")

    replace_readme()


if __name__ == "__main__":
    main()