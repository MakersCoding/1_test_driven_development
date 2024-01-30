import pytest
from lib.present import Present

"""
Tests when we wrap an item and then unwrap said item
"""

def test_has_anything_been_wrapped():
    present = Present()
    present.wrap("Xbox")
    assert present.unwrap() == "Xbox"
     

"""
Raises an error message if contents has already been wrapped

"""

def test_error_message_if_contents_has_been_wrapped():
    present = Present()
    present.wrap("Xbox")
    with pytest.raises(Exception) as err:
        present.wrap('Xbox Game')
    error_message = str(err.value)
    assert error_message == "A contents has already been wrapped."
    

"""
Raises an error when upnwrapping a present before wrapping

"""

def test_error_message_if_contents_is_none():
    present = Present()
    with pytest.raises(Exception) as err:
        present.unwrap()
    error_message = str(err.value)
    assert error_message == "No contents have been wrapped."    


"""
Tests to ensure re-wrapping an item does not replace the initially wrapped item

"""

def test_if_rewrapped_item_replaces_intially_wrapped_item():
    present = Present()
    present.wrap("Xbox")
    with pytest.raises(Exception) as err:
        present.wrap('Lump of Coal')
    assert present.unwrap() == "Xbox"
    
    