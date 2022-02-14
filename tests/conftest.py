import sys

from pytest import fixture


# Each test runs on cwd to its temp dir
@fixture(autouse=True)
def go_to_tmpdir(request, tmpdir):
    # Ensure local test created packages can be imported
    sys.path.insert(0, str(tmpdir))
    with tmpdir.as_cwd():  # Chdir only for the duration of the test.
        yield
