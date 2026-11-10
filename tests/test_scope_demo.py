import pytest

@pytest.fixture(scope="function")
def per_test():
    print("\n  [function] SETUP - runs before EVERY test")
    yield
    print("\n  [function] TEARDOWN - runs after EVERY test")

@pytest.fixture(scope="module")
def per_file():
    print("\n[module] SETUP - runs ONCE per file")
    yield
    print("\n[module] TEARDOWN - runs once after the last test in the file")

def test_one(per_file, per_test):
    print("  running test_one")

def test_two(per_file, per_test):
    print("  running test_two")