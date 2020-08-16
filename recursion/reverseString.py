def reverseString(string):
    print(string)
    if len(string) == 0:
        return string
    else:
        return reverseString(string[1::])+string[0]


# o(n)
def iterativeReverse(string):
    reversestring = ''
    for i in range(len(string)):
        reversestring = reversestring+string[len(string)-i-1]
    return reversestring


print(reverseString("heyyyya"))
print(iterativeReverse("Whodidit"))
