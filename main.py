import requests
import sys
import os

def get_diff(repo_name, version_hash, file_path):
    # Construct the URL for the diff
    url = f"https://api.github.com/repos/{repo_name}/compare/{version_hash}...main"

    # Check if a GitHub API token is set
    token = os.environ.get('GITHUB_API_TOKEN')
    headers = {}
    if token:
        headers['Authorization'] = f'token {token}'

    # Make the request to the GitHub API
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an error if the request failed

    # Parse the response JSON
    data = response.json()
    files = data.get('files', [])

    # Filter out non-language files and print the diffs
    for file in files:
        if file['filename'].endswith(('.ts', '.js', '.dart', '.go', '.java', '.kt')):
            #print(f"Diff for {file['filename']}:\n{file['patch']}\n")
            print(f"Diff for {file['filename']} found.")
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <repository_name> <version_hash> <file_path>")
        sys.exit(1)

    repo_name = sys.argv[1]
    version_hash = sys.argv[2]
    file_path = sys.argv[3]

    get_diff(repo_name, version_hash, file_path)
