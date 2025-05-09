import re
from django.core.exceptions import ValidationError


def check_phone(value):
    """
    Validate the phone number based on Iranian format
    :param: a string
    :return: True/False
    """
    patter1 = re.compile(r"^9\d{9}$")
    patter2 = re.compile(r"^09\d{9}$")
    patter3 = re.compile(r"^00989\d{9}$")
    patter4 = re.compile(r"^\+989\d{9}$")

    if bool(patter1.match(value)):
        return "0" + value
    if bool(patter2.match(value)):
        return value
    if bool(patter3.match(value)):
        return "0" + value[4:]
    if bool(patter4.match(value)):
        return "0" + value[3:]

    raise ValidationError(f'{value} is not a valid phone')
