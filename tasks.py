from invoke import task

@task
# Run DNA analysis with test fasta because no UI yet.
def start(ctx):
    ctx.run("python3 src/run_dna.py src/testfasta/testi.fasta", pty=True)

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
    ctx.run("python3 -m pylint src", pty=True)


@task
def run_json(ctx):
    """Run the CLI and save results as JSON to out.json."""
    ctx.run("python3 src/run_dna.py src/testfasta/testi.fasta --gc-profile --save-results out.json", pty=True)


@task
def run_csv(ctx):
    """Run the CLI and save results as CSV to out.csv."""
    ctx.run("python3 src/run_dna.py src/testfasta/testi.fasta --gc-profile --save-results out.csv", pty=True)


@task
def gui(ctx):
    """Launch the Tkinter GUI for the DNA tool."""
    ctx.run("python3 src/gui.py", pty=True)
