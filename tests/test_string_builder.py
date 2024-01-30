from lib.string_builder import StringBuilder

"""
Ouptuts an empty string if no string is added to add

"""

def test_empty_string():
    string_builder = StringBuilder()
    result = string_builder.output()
    assert result == ""



# Below test is redundant since its testing function is already tested in a later test 
#"""
#Adds one string and checks the output is correct

#"""

#def test_string_builder_adds_single_string():
#    string_builder = StringBuilder()
#    string_builder.add("Hello World!")
#    result = string_builder.output()
#    assert result == "Hello World!"

"""
Adds multiple strings and checks the output is correct

"""
def test_string_builder_adds_multiople_strings():
    string_builder = StringBuilder()
    string_builder.add("Hello World!")
    string_builder.add(" I'm Alive :)")
    result = string_builder.output()
    assert result == "Hello World! I'm Alive :)"

"""
Tests the length of a single string

"""    

def test_string_length():
    string_builder = StringBuilder()
    string_builder.add("Hello World!")
    result = string_builder.size()
    assert result == 12

"""
Tests the length of a multiple strings

"""    

def test_string_builder_test_length_of_multiople_strings():
    string_builder = StringBuilder()
    string_builder.add("Hello World!")
    string_builder.add(" I'm Alive :)")
    result = string_builder.size()
    assert result == 25