import requests
import sys
import os
import re


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

    # Combine the diffs into one string
    combined_diff = ""
    for file in files:
        if file['filename'].endswith(('.ts', '.js', '.dart', '.go', '.java', '.kt')):
            combined_diff += f"Diff for {file['filename']}:\n{file['patch']}\n\n"

    return combined_diff


from openai import OpenAI
import os

def apply_changes_to_file(diff, file_path):
    # Load the content of the file
    with open(file_path, 'r') as file:
        file_content = file.read()

    # Construct the messages for ChatGPT
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Here is a diff of some relevant files that show changes in an API:\n\n{diff}\n\nI want you to take them and then apply these changes to a file that follows:\n\n{file_content}\n\nPlease return the file with the refactoring applied, and nothing else."}
    ]

    # Set the OpenAI API key
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable is not set.")

    # Initialize the OpenAI client
    client = OpenAI(api_key=api_key)

    # Call the OpenAI ChatGPT-4 API
    completion = client.chat.completions.create(
        model="gpt-4-0125-preview",
        messages=messages,
        max_tokens=2048,
        temperature=0.7
    )

    # Extract the refactored file content from the response
    refactored_file_content = completion.choices[0].message.content


    # Use a regular expression to remove the opening and closing code block delimiters
    refactored_file_content = re.sub(r'^```[a-zA-Z]+\n', '', refactored_file_content, count=1)  # Remove opening delimiter
    refactored_file_content = re.sub(r'\n```$', '', refactored_file_content, count=1)  # Remove closing delimiter



    # Write the refactored content back to the file
    with open(file_path, 'w') as file:
        file.write(refactored_file_content)

    return refactored_file_content
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <repository_name> <version_hash> <file_path>")
        sys.exit(1)

    repo_name = sys.argv[1]
    version_hash = sys.argv[2]
    file_path = sys.argv[3]

    diff = get_diff(repo_name, version_hash, file_path)
    refactored_file_content = apply_changes_to_file(diff, file_path)
    print(refactored_file_content)
