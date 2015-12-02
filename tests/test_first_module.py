import pytest

from first_package import first_module


class FirstModuleTests:

    def test_sum(self):
        result = first_module.sum(1, 1)
        assert 2 == result


def test_div():
    assert 1 == first_module.div(2, 2)
