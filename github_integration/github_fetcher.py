import requests



def parse_repo_url(repo_url):
    parts = repo_url.rstrip("/").split("/")
    owner = parts[-2]
    repo = parts[-1]
    return owner, repo


def get_python_files(owner, repo):
    """
    Fetch all Python files from a public GitHub repository.
    """

    api_url = f"https://api.github.com/repos/{owner}/{repo}/contents"

    python_files = []

    def traverse(url):

        response = requests.get(url)

        if response.status_code != 200:
            return

        contents = response.json()

        for item in contents:

            if item["type"] == "file" and item["name"].endswith(".py"):
                python_files.append(item["download_url"])

            elif item["type"] == "dir":
                traverse(item["url"])

    traverse(api_url)

    return python_files

def get_file_content(download_url):

    response = requests.get(download_url)

    if response.status_code == 200:
        return response.text

    return None


