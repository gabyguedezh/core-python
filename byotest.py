def number_of_evens(numbers):
    return 0
    
def odd_numbers(numbers):
    odds = 0
    odd_numbers = []
    for n in numbers:
        if n % 2 != 0:
            odds += 1
            odd_numbers.append(n)
    if odds != 0:
        return odd_numbers
    else:
        return False
   
pets = ["dog", "cat", "rabbit"] 
wild = ["fox", "wolf", "tiger"]
all_animals = pets+wild
def cute_animals(animals):
    return all_animals
    
    
def test_are_equal(expected, actual):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)

def test_not_equal(a, b):
    assert a != b, "Expected {0}, but got {1}".format(a, b)
    
def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)

def test_not_in(collection, item):
    assert item not in collection, "{0} does contain {1}, try another animal to see if it's not on the list".format(collection, item)

def test_between(between, value):
    lower = min(between)
    upper = max(between)
    between = range(lower, upper)
    assert value in between, "{0} is not between {1}".format(value, between)
   

test_are_equal(number_of_evens([1,2,3,4,5]), 0)
test_not_equal(number_of_evens([1,2,3,4,5]), 2)

test_is_in(cute_animals(all_animals), "wolf")
test_not_in(cute_animals(all_animals), "coyote")

# test_between(number_of_evens([1,2,3,4,5]), 12)
test_between([0, 6], 4)
test_between(odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]), 4)



print("All test passed!")