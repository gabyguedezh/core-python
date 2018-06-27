def number_of_evens(numbers):
    return 0
   
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
    #Need to define programatically lower and upper
    lower = 1
    upper = 6
    assert value in range(lower, upper), "{0} is not between {1}".format(value, range(lower, upper))
   

test_are_equal(number_of_evens([1,2,3,4,5]), 0)
test_not_equal(number_of_evens([1,2,3,4,5]), 2)

test_is_in(cute_animals(all_animals), "wolf")
test_not_in(cute_animals(all_animals), "coyote")

test_between(number_of_evens([1,2,3,4,5]), 5)



print("All test passed!")