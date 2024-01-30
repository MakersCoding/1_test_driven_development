from lib.gratitudes import Gratitudes 

"""
Adds no strings and returns formatted  

"""

def test_gratitude_formatting_adds_no_strings():
    gratitude_formatting = Gratitudes()
    result = gratitude_formatting.format()
    assert result == 'Be grateful for: '

"""
Adds multiple strings to the gratitude list and prints them formatted 

"""

def test_gratitude_formatting_adds_multiple_strings():
    gratitude_formatting = Gratitudes()
    gratitude_formatting.add("Extra Time")
    gratitude_formatting.add('Breaks')
    result = gratitude_formatting.format()
    assert result == 'Be grateful for: Extra Time, Breaks'