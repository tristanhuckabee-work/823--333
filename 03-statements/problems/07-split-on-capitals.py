# Create a function which adds spaces before every capital in a word. Lower case
# the whole string afterwards.

# Write your function here.
def cap_space(str):
    res = ''

    for char in str:
        lw = char.lower()
        if char == lw:
            res += char
        else:
            res += ' ' + lw
    return res


print(cap_space("helloWorld"))     #> "hello world"
print(cap_space("iLoveMyTeapot"))  #> "i love my teapot"
print(cap_space("stayIndoors"))    #> "stay indoors"