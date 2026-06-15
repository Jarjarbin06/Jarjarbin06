import os
import requests
from datetime import datetime

USERNAME = os.getenv("USERNAME")
IGNORED = os.getenv("GH_IGNORED_REPO")
TOKEN = os.getenv("GH_TOKEN")

IGNORED = IGNORED.split(" ") if IGNORED else []

HEADERS = {
    "Authorization": f"token {TOKEN}"
}


# -----------------------------
# HELPERS
# -----------------------------
def gh_get(url):
    r = requests.get(url, headers=HEADERS)
    r.raise_for_status()
    return r.json()


def contained(str_name: str, list_names: list[str]):
    for name in list_names:
        if name in str_name:
            return True
    return False


def safe_get_file(repo_url, filename):
    """
    Fetch file content from GitHub repo root safely.
    """
    try:
        contents = gh_get(repo_url + "/contents")
        for file in contents:
            if file["name"] == filename:
                return requests.get(file["download_url"]).text.strip()
    except:
        return None
    return None


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

    active = [
        r for r in repos
        if (datetime.utcnow() - datetime.strptime(r["pushed_at"], "%Y-%m-%dT%H:%M:%SZ")).days < 30
    ]

    out += "\n## 🔹 Active Repositories (30 days)\n"
    for repo in active:
        out += f"- {repo['name']}\n"

    return out


# -----------------------------
# 3. METADATA SYSTEM
# -----------------------------
def extract_repo_metadata(repo):
    result = {
        "version": "![version](https://img.shields.io/badge/version-unknown-black?style=flat-square)",
        "status": "![status](https://img.shields.io/badge/status-unknown-black?style=flat-square)",
        "badges": [],
        "url": ""
    }

    try:
        contents = gh_get(repo["url"] + "/contents")
        result["url"] = repo["html_url"]

        for file in contents:
            name = file["name"]
            raw = None

            # VERSION
            if name == "VERSION":
                raw = requests.get(file["download_url"]).text
                result["version"] = f"![version](https://img.shields.io/badge/version-{raw.splitlines()[0].strip()}-7c7c7c?style=flat-square)"

            # STATUS
            elif name == "STATUS":
                raw = requests.get(file["download_url"]).text
                result["status"] = raw.splitlines()[0].strip()

            # BADGES
            elif name == "BADGES":
                raw = requests.get(file["download_url"]).text
                result["badges"] = [
                    line.strip()
                    for line in raw.splitlines()
                    if line.strip().startswith("!")
                ]

    except:
        pass

    return result


def generate_metadata(repos):
    out = "# 🧩 Metadata Tracking\n\n"

    for repo in repos:
        name = repo["name"]

        if name in IGNORED:
            continue

        meta = extract_repo_metadata(repo)

        out += f"## 🔹 {}\n"
        out += "> ### Info:\n"
        out += f"> {meta['version']}  \n"
        out += f"> {meta['status']}  \n"

        if meta["badges"]:
            out += "> \n> ### Description:\n"
            for b in meta["badges"]:
                out += f"> - {b}\n"
        else:
            out += "> ### Description: none\n"

        out += "\n"

    return out


# -----------------------------
# README SAVER
# -----------------------------
def replace_readme():
    with open("README_template.md", 'r') as file:
        readme = file.read()

    with open("generated/projects.md", 'r') as file:
        projects = file.read()

    readme = readme.replace("<!-- GENERATED:PROJECTS -->", projects)

    with open("generated/activity.md", 'r') as file:
        activity = file.read()

    readme = readme.replace("<!-- GENERATED:ACTIVITY -->", activity)

    with open("generated/metas.md", 'r') as file:
        metas = file.read()

    readme = readme.replace("<!-- GENERATED:METAS -->", metas)

    with open("README.md", 'w') as file:
        file.write(readme)


# -----------------------------
# MAIN
# -----------------------------
def main():
    print(f"username found ? {bool(USERNAME)}\ntoken found ? {bool(TOKEN)}")

    repos = gh_get(f"https://api.github.com/users/{USERNAME}/repos?per_page=100")
    starred = gh_get(f"https://api.github.com/users/{USERNAME}/starred?per_page=100")

    print(f"{len(repos)=}")
    print(f"{len(starred)=}")
    print(f"{IGNORED=}")

    os.makedirs("generated", exist_ok=True)

    with open("generated/projects.md", "w") as f:
        f.write(generate_projects(repos))

    with open("generated/activity.md", "w") as f:
        f.write(generate_activity(repos))

    with open("generated/metas.md", "w") as f:
        f.write(generate_metadata(repos))

    replace_readme()


if __name__ == "__main__":
    main()
