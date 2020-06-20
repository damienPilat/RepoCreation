import os
import sys
from github import Github
import pygit2

# Path for new folder
path = "YOUR_LOCAL_PATH"
username = "YOUR_USERNAME"
password = "YOUR_PASSWORD"


def readMe_contents(repo_name):
    """
    Contents of readMe.txt file
    :param repo_name:
    :return:
    """
    return str("--------------------------------------------\n" \
               "Initial Commit for project {}\n" \
               "--------------------------------------------".format(repo_name))


def createRepo():
    """
    Get folder name from terminal input,
    Retrieve Git user account,
    Create repo in user account,
    Add readMe file,
    Clone to local path
    """
    # Get repo name from user input
    repo_name = str(sys.argv[1])

    # Connect to Github
    user = Github(username, password).get_user()
    # Create repo and add readMe
    repo = user.create_repo(repo_name)
    repo.create_file("readMe.txt", "initial commit", readMe_contents(repo_name))
    # Clone Repo
    pygit2.clone_repository(repo.git_url, '../'+repo_name)

    # Print: Repo created
    print("Repo '{}' successfully created".format(repo_name))


if __name__ == "__main__":
    createRepo()
