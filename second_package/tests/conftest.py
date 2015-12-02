import pytest


@pytest.fixture
def name():
    return 'totsSomJordi.txt'


@pytest.fixture
def file_with_name(name):
    print(name)
    return open(name, 'a')
