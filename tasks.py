from invoke import task

@task
# Run DNA analysis with test fasta because no UI yet.
def start(ctx):
    ctx.run("python3 src/run_dna.py src/testfasta/testi.fasta", pty=True)

@task
def test(ctx):
    # run tests located under src/tests
    ctx.run("pytest src/tests", pty=True)

@task
def coverage(ctx):
    # run coverage over tests under src/tests
    ctx.run("coverage run --branch -m pytest src/tests", pty=True)


@task
def coverage_report(ctx):
    """Run coverage and produce HTML report (htmlcov/index.html)."""
    ctx.run("coverage run --branch -m pytest src/tests", pty=True)
    ctx.run("coverage html", pty=True)
