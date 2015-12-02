import sys

import pytest

from first_package import first_module


def test_exception_div_42():
    with pytest.raises(ZeroDivisionError) as e:
        first_module.div(42, 0)


def test_raises_exception():
    with pytest.raises(first_module.CustomError) as exc:
        first_module.raises_custom('TOOLS')
    assert 'Raise for TOOLS' in str(exc.value)


@pytest.mark.skipif(True, reason='This fails :)')
def test_exception_div():
    with pytest.raises(ZeroDivisionError) as e:
        first_module.div(42, 3)


@pytest.mark.xfail(sys.version_info >= (3, 0), reason='This test fails')
def test_print():
    assert 0
