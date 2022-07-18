from invoke import task
import os 

HERE = os.path.abspath(os.path.dirname(__file__))

@task
def build(ctx):
    """Build the cookiecutter."""
    ctx.run(f"python cookiecutter_spec.py {HERE} --no-input")
