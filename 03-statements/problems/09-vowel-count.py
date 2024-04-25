# Create a function called `vowel_count` that takes in a string and returns a
# count of how many vowels are in the string.

# Write your solution here.
def vowel_count(str):
    vowels = 'aeiou'
    total = 0
    for vowel in vowels:
        total += str.lower().count(vowel)

    return total


print(vowel_count("App Academy"))         #> 4
print(vowel_count("Coding Expert"))       #> 4
print(vowel_count("Supreme"))             #> 3
print(vowel_count("Chamber of Secrets"))  #> 5