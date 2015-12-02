import boto3
import pytest


@pytest.fixture(scope='module')
def file(request):
    print('opening file')
    file_ = open('test_file.txt', 'a')

    def fin():
        print('closing file')
        file_.close()

    request.addfinalizer(fin)
    return file_
