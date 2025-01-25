# tasks.py
from invoke import task


@task(default=True)
def run(ctx):
    ctx.run(f"streamlit run index.py", pty=True)

@task
def gen(ctx):
    ctx.run(f"python min_gen.py", pty=True)    