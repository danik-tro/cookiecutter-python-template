import os


def post_gen_function():
    """Post gen function for template"""
    # Initialize repository after generating project
    os.system("git init")
    os.system("git config user.name \"{{cookiecutter.author}}\"")
    os.system("git config user.email \"{{cookiecutter.email}}\"")
    # Install project dependency
    # Install pre-commit
    os.system("make setup")


if __name__ == "__main__":
    post_gen_function()
