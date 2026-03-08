import unittest
from validating_code import form_username

def test_form_username():
    assert form_username("1yogabagaba.SmileFF")==True

def test_wrong_form_username():
    assert form_username("yogabagaba")==False