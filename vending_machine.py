from byotest import *

#This function will apply if there's no change to be given
def get_change(amount):
    #If there's no change to give, no coins will be given back
    if amount == 0:
        return []
    #What if we need to give coins back...
    #For when one coin of a given denomination would match the change exactly...
    if amount in [100, 50, 20, 10, 5, 2, 1]:
        return [amount]
    #If we need to give a 2 and a 1 to give 3 cents change
    change = []
    #if the coins are less than or equal to the amount we need to return, 
    #just add them to the change
    for coin in [100, 50, 20, 10, 5, 2, 1]:
        #This was previously an if statement but changed to a while to account 
        #occasions in which more than one coin of a denomination are needed
        while coin <= amount:
            #we need to deduct the amount from the coin from the amount that we
            #sent in to avoid it calculating as change any coin of a lower 
            #denomination than the amount (in the case of a wanted change of 7 
            #cents, this would prevent it from returning a 5 a 2 and a 1!)
            amount -= coin
            change.append(coin)
            
    return change
    

#When no change is required, no coins will be given
test_are_equal(get_change(0), [])

#The next situation will be when the change required can be resolved
#with a single one cent coin
test_are_equal(get_change(1), [1])

#Now, we test what happens if we need to give one coin of a higher value back
test_are_equal(get_change(2), [2])

#Then, we keep going and write tests for every possible coin denomination
test_are_equal(get_change(5), [5])
test_are_equal(get_change(10), [10])
test_are_equal(get_change(20), [20])
test_are_equal(get_change(50), [50])
test_are_equal(get_change(100), [100])

#And what happens if we need to give back more than one coin?
#Let's pass our get_change function a value of 3 and expect a 2 and a 1 back
test_are_equal(get_change(3), [2,1])
test_are_equal(get_change(7), [5,2])

#What happens if we need to give more than one coin of a particular denomination
test_are_equal(get_change(9), [5,2,2])

print("All tests pass!")