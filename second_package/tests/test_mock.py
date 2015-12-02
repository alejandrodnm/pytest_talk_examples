import pytest

from second_package import my_second_module


def test_no_mock():
    assert my_second_module.to_test_1(1) == 1


def test_simple_mock(mocker):
    to_mock = mocker.patch('second_package.my_second_module.to_mock', return_value=2)
    assert my_second_module.to_test_1(1) == 2
    print(to_mock.call_args)
    to_mock.assert_called_once_with(1)


def test_simple_mock_2(mocker):
    class_instance = mocker.Mock()
    class_instance.value = 2
    assert my_second_module.to_test_2(class_instance) == 4


def test_side_effect(mocker):
    boto3 = mocker.patch('second_package.my_second_module.boto3')

    def side_effect(key):
        if not key.startswith('s3'):
            raise ValueError
    get_key_mock = mocker.Mock(side_effect=side_effect)
    boto3.get_key = get_key_mock
    key = 'wrong_key'
    msg = my_second_module.to_test_boto(key)
    assert msg == 'wrong_key'


def test_boto3(mocker):
    boto3 = mocker.patch('second_package.my_second_module.boto3')
    response = mocker.Mock()
    response.value = 'uploaded'
    boto3.session.Session().resource.upload.return_value = response

    assert my_second_module.boto_3(**{'bucket': 'b'}) == 'uploaded'
    assert boto3.session.Session.called
