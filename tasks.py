from invoke import task

@task
def start(ctx):
    # Launch the Tkinter GUI
    ctx.run("python3 src/gui.py", pty=True)

@task
def test(ctx):
    # run tests under the top-level `tests` directory only
    ctx.run("pytest tests", pty=True)

@task
def coverage(ctx):
    # run coverage over tests under the top-level tests directory
    ctx.run("coverage run --branch -m pytest tests", pty=True)


@task
def coverage_report(ctx):
    #Run coverage and produce HTML report (htmlcov/index.html).
    ctx.run("coverage run --branch -m pytest tests", pty=True)
    ctx.run("coverage html", pty=True)


@task
def pylint(ctx):
    #Run pylint on src.
    ctx.run("python3 pylint src", pty=True)
