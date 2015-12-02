import pytest

from first_package import first_module


@pytest.mark.parametrize('x, y', [(3, 2), (1, 4), (10, 20)])
def test_multiple_sums(x, y):
    print(x, y)
    assert x + y == first_module.sum(x, y)


def test_other_module_fixture(file):
    assert True
