import boto3


def to_mock(a):
    print('I was here')
    return a


def to_test_1(a):
    return to_mock(a)


def to_test_2(class_instance):
    a = class_instance.value
    return 2 * class_instance.value


def to_test_boto(key):
    try:
        boto3.get_key(key)
    except ValueError:
        return 'wrong_key'


def boto_3(**settings):
    session = boto3.session.Session(**settings)
    s3 = session.resource
    response = s3.upload()
    return response.value
