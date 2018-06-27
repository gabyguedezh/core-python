def is_even_number(number):
        return number % 2 == 0
        
def even_number_of_evens(numbers):

    even_evens = sum([1 for number in numbers if is_even_number(number)])
    return False if even_evens == 0 else is_even_number(even_evens)

# def is_even(number):
#     return number % 2 == 0

# def even_number_of_evens(numbers):
    
#     evens = sum([1 for n in numbers if is_even(n)])
#     return False if evens == 0 else is_even(evens)

        

assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([2]) == False, "One even number"
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Multiple numbers, three are even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, four are even"
assert even_number_of_evens([1, 3, 9]) == False, "No even numbers"

print("All tests passed!")