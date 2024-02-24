import git
import os
import shutil

def git_push(repo_path, file_or_directory, commit_message, external_files=[]):
    try:
        # Change directory to the Git repository
        os.chdir(repo_path)

        # Initialize a Git repository object
        repo = git.Repo()

        # Copy external files into repository directory
        for external_file in external_files:
            shutil.copy(external_file, repo_path)

        # Add the specified file or directory to the staging area
        repo.git.add(file_or_directory)

        # Commit changes
        repo.git.commit('-m', commit_message)

        # Push changes to the remote repository
        origin = repo.remote(name='origin')
        origin.push()

        print("Pushed to Git successfully.")

    except Exception as e:
        print("Error occurred while pushing to Git:", e)

if __name__ == "__main__":
    # Ask user for repository path
    repo_path = input("Enter the path to your Git repository: ")

    # Ask user for file or directory to be pushed
    file_or_directory = input("Enter the file or directory to be pushed: ")

    # Ask user for commit message
    commit_message = input("Enter commit message: ")

    # Predefined list of external files to be included in the commit
    external_files = [
        r'D:\sandbox_not_pushed\Validation_Gen6\src\rad600\rof\ric\testcases\ARS\RoadType\test.py',
        # '/path/to/external/file2.txt'
    ]

    git_push(repo_path, file_or_directory, commit_message, external_files)
