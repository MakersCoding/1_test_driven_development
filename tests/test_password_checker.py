import pytest
from lib.password_checker import PasswordChecker

"""
Test if password contains exactly eight characters

"""

def test_if_password_contains_eight_characters():
    password_checker = PasswordChecker()
    assert password_checker.check("password") == True

"""
Test if password contains eight or more characters 

"""

def test_if_password_contains_eight_or_more_characters():
    password_checker = PasswordChecker()
    assert password_checker.check("password1") == True


"""
Produce error message if password is less than 8 characters and thus invalid

"""

def test_produce_error_message_if_password_invalid():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as err:
        password_checker.check("passwor")
    assert str(err.value) == "Invalid password, must be 8+ characters."

    
