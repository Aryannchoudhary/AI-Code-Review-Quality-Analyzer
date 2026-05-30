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

    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "AI-Code-Analyzer"
    }

    response = requests.get(url, headers=headers)

    print("URL:", url)
    print("Status Code:", response.status_code)

    if response.status_code != 200:
        print("Error:", response.text)
        return

    contents = response.json()

    for item in contents:

        print(item["name"], item["type"])

        if item["type"] == "file" and item["name"].endswith(".py"):

            print("FOUND PYTHON FILE:", item["name"])

            python_files.append(
                item["download_url"]
            )

        elif item["type"] == "dir":

            traverse(
                item["url"]
            )

def get_file_content(download_url):

    response = requests.get(download_url)

    if response.status_code == 200:
        return response.text

    return None


