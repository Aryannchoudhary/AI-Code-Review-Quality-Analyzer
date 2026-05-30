import requests
import json

def parse_repo_url(repo_url):
    parts = repo_url.rstrip("/").split("/")
    owner = parts[-2]
    repo = parts[-1].replace(".git", "")
    return owner, repo

def get_python_files(owner, repo):
    api_url = f"https://api.github.com/repos/{owner}/{repo}/contents"

    python_files = []

    def traverse(url):
        response = requests.get(url)

        if response.status_code != 200:
            return

        contents = response.json()

        for item in contents:
            if item["type"] == "file" and (
                 item["name"].endswith(".py")
                 or item["name"].endswith(".ipynb")
            ):
                python_files.append(item["download_url"])

            elif item["type"] == "dir":
                traverse(item["url"])

    traverse(api_url)

    return python_files

def get_file_content(download_url):

    response = requests.get(download_url)

    if response.status_code != 200:
        return None

    # Python file
    if download_url.endswith(".py"):
        return response.text

    # Jupyter Notebook
    elif download_url.endswith(".ipynb"):

        notebook = response.json()

        code = []

        for cell in notebook.get("cells", []):

            if cell.get("cell_type") == "code":

                code.append(
                    "".join(cell.get("source", []))
                )

        return "\n".join(code)

    return None

