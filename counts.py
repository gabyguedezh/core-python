"""
def count_upper_case(message):
    count = 0
    for c in message:
        if c.isupper():
            count += 1
    return count

# print(count_upper_case("Hello World"))

"""
#Changed the function for the one given in the challenge to test
def count_upper_case(message):
    #return add +1 per character in message if the character is upper case
    return sum([1 for c in message if c.isupper()])

assert count_upper_case("") == 0, "Empty String"
assert count_upper_case("A") == 1, "One upper case"
assert count_upper_case("a") == 0, "One lower case"
assert count_upper_case("£$%%^") == 0, "Special characters"
#Added tests according to the challenge
assert count_upper_case("AA") == 2, "Two upper cases"
assert count_upper_case("A1") == 1, "One upper case and a number"

print("All the tests passed")