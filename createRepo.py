import os
import sys
from github import Github

# Path for new folder
path = "YOUR_PATH"
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
    Create folder in specified path,
    Retrieve Git user account,
    Create repo in user account.
    """
    repo_name = str(sys.argv[1])
    os.makedirs(path + repo_name)
    file_path = os.path.join(path, repo_name, 'readMe.txt')
    f = open(file_path, "x")
    f.write(readMe_contents(repo_name))
    user = Github(username, password).get_user()
    repo = user.create_repo(repo_name)
    repo.create_file("readMe.txt", "initial commit", readMe_contents(repo_name))

    # Print: Repo created
    print("Repo '{}' successfully created".format(repo_name))


if __name__ == "__main__":
    createRepo()
