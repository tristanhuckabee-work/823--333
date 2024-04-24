# You are given three inputs: a string, one letter, and a second letter.

# Write a function that returns `True` if every instance of the first letter
# occurs before every instance of the second letter.

# Look at the String Methods to possibly help you find some methods that can
# make this easier.
# https://docs.python.org/3.9/library/stdtypes.html?highlight=strings#string-methods

# Write your function here.
def first_before_second(str, sub1, sub2):
    return str.rfind(sub1) < str.find(sub2)
    
    # idx1 = str.index(sub1)
    # idx2 = str.index(sub2)

    # try:  
    #     temp = str.index(sub1, idx2)
    #     return False
    # except:
    #     return True

    # return str.index(sub1) < str.index(sub2)




print(first_before_second("a rabbit jumps joyfully", "a", "j"))
#> True
# Every instance of "a" occurs before every instance of "j".

print(first_before_second("knaves knew about waterfalls", "k", "w"))
#> True

print(first_before_second("happy birthday", "a", "y"))
#> False
# The "a" in "birthday" occurs after the "y" in "happy".

print(first_before_second("precarious kangaroos", "k", "a"))
#> False

