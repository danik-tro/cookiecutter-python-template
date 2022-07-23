import os


def post_gen_function():
    """Post gen function for template"""
    # Initialize repository after genereting project
    os.system("git init")



if __name__ == "__main__":
    post_gen_function()