from lib.counter import Counter

"""

Initially reports a count of 0

"""
def test_counter_zero():
    counter = Counter()
    result = counter.report() 
    assert result == "Counted to 0 so far."

"""

Countes to 10 from 0 in increments of 1 using multiple numbers

"""

def test_counter_counts_to_ten_from_0():
    counter = Counter()
    counter.add(1)
    counter.add(1)
    counter.add(1)
    counter.add(1)
    counter.add(1)
    counter.add(1)
    counter.add(1)
    counter.add(1)
    counter.add(1)
    counter.add(1)
    result = counter.report()
    assert result == "Counted to 10 so far."


"""
Counts to five from 0 in increments of five

"""

def test_counter_count_to_five(): 
    counter = Counter()
    counter.add(5)
    result = counter.report()
    assert result == "Counted to 5 so far."

"""
Counts to to -10 using multiple different numbers

"""

def test_counter_count_to_minus_ten_using_multiple_numbers(): 
    counter = Counter()
    counter.add(-4)
    counter.add(-6)
    result = counter.report()
    assert result == "Counted to -10 so far."


