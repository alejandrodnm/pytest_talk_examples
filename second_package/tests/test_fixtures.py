import pytest


def test_file_fix(file):
    file.write('test_file_fix')


def test_file_2_fix(file):
    file.write('test_file_2_fix')


def test_file_with_name(file_with_name):
    file_with_name.write('test_file_with_name')


@pytest.mark.parametrize('name', ['foreverSpam.txt', 'weWillBurn.txt'])
def test_file_with_name_parametrize(file_with_name):
    file_with_name.write('test_file_with_name')
