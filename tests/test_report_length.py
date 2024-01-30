from lib.report_length import *

def test_report_length_long():
    result = report_length('long')
    assert result == f"This string was {4} characters long."

def test_report_length_hello_world():
    result = report_length('hello world')
    assert result == f"This string was {11} characters long."

def test_report_length_long_alphabet():
    result = report_length('abcdefghijklmnopqrstuvwxyz')
    assert result == f"This string was {26} characters long."

def test_report_length_custom():
    result = report_length("custom")
    result2 = len("custom")
    assert result == f"This string was {result2} characters long."