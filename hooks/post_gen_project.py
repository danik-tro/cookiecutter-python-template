import os
from pathlib import Path


def post_gen_function():
    """Post gen function for template"""
    # Initialize repository after generating project
    os.system("git init")
    os.system("git config user.name \"{{cookiecutter.author}}\"")
    os.system("git config user.email \"{{cookiecutter.email}}\"")
    # Install project dependency
    # Install pre-commit
    os.system("make setup")

    # Remove py.typed if library is not type supported
    if "{{ cookiecutter.typed_library }}" == "N":
        file_to_remove = Path(os.getcwd()) / "{{cookiecutter.app_name}}" / "py.typed"
        os.remove(file_to_remove)


if __name__ == "__main__":
    post_gen_function()
