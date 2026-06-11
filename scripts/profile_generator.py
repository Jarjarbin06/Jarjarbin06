import os
import requests
from datetime import datetime

USERNAME = "Jarjarbin06"
TOKEN = os.getenv("GH_TOKEN")

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

    for repo in repos:
        name = repo["name"]
        url = repo["html_url"]
        lang = repo["language"] or "Unknown"
        updated = repo["updated_at"]

        language_map[lang] = language_map.get(lang, 0) + 1

        category = "misc"
        if "lib" in name:
            category = "libraries"
        elif "tool" in name or "JCCS" in name:
            category = "tools"
        elif "Makefile" in name or "epitech" in name:
            category = "framework"

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

    with open("generated/projects.md", 'r') as file:
        projects = file.read()

    readme = readme.replace(
        "<!-- GENERATED:PROJECTS -->",
        projects
    )

    with open("generated/activity.md", 'r') as file:
        activity = file.read()

    readme = readme.replace(
        "<!-- GENERATED:ACTIVITY -->",
        activity
    )

    with open("generated/versions.md", 'r') as file:
        versions = file.read()

    readme = readme.replace(
        "<!-- GENERATED:VERSIONS -->",
        versions
    )

    try:
        with open("README.md", 'x') as file:
            file.write(readme)
    except FileExistsError:
        with open("README.md", 'w') as file:
            file.write(readme)


# -----------------------------
# MAIN
# -----------------------------
def main():
    repos = gh_get(f"https://api.github.com/users/{USERNAME}/repos?per_page=100")

    os.makedirs("generated", exist_ok=True)

    with open("generated/projects.md", "w") as f:
        f.write(generate_projects(repos))

    with open("generated/activity.md", "w") as f:
        f.write(generate_activity(repos))

    with open("generated/versions.md", "w") as f:
        f.write(generate_versions(repos))


if __name__ == "__main__":
    main()