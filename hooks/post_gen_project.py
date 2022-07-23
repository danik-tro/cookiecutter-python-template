import os


def post_gen_function():
    """Post gen function for template"""
    # Initialize repository after genereting project
    os.system("git init")
    # Install project dependency
    # Install pre-commit
    os.system("make setup")



if __name__ == "__main__":
    post_gen_function()