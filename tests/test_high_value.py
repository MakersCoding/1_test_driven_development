from lib.high_value import *
"""
check if the first value is higher than second value
"""
def test_first_value_higher_than_second():
    test_high_value = HighValue(10, 5)
    assert test_high_value.get_highest() == "First value is higher"
"""
check if the second value is higher than first value
"""
def test_first_value_lower_than_second():
    test_high_value = HighValue(5, 10)
    assert test_high_value.get_highest() == "Second value is higher"
"""
check if the values are equal
"""
def test_first_value_equal_to_second():
    test_high_value = HighValue(10, 10)
    assert test_high_value.get_highest() == "Values are equal"
"""
check adding number to first value and returning value increased by number
"""
def test_adding_seven_to_first():
    test_high_value = HighValue(10, 5)
    test_high_value.add(7, "first")
    assert test_high_value.value_first == 17
"""
check adding number to second value and returning value increased by number
"""
def test_adding_seven_to_second():
    test_high_value = HighValue(10, 5)
    test_high_value.add(7, "second")
    assert test_high_value.value_second == 12
"""
check adding float negative number to zero value and seeing which is higher
"""
def test_adding_minus_floats_to_zero():
    test_high_value = HighValue(0, 0)
    test_high_value.add(-7.5, "second")
    assert test_high_value.get_highest() == "First value is higher"