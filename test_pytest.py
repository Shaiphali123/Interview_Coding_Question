import pytest

@pytest.fixture
def setup():
    print("Setup process")
    yield
    print("Teardown process")

def test_example(setup):
    assert True