
name = "Hi my name is ebi"


# 1
print(name[::-1])


# 2
def reverseString(str):

    # if not str or len(str) < 2:
    #     return "nope not it"

    backwards = []
    totalitems = len(str)-1

    # **RANGE (#*? create a sequence of # from 16 to -2, but increment by -1
    for i in range(totalitems, -1, -1):
        backwards.append(str[i])

    # print(backwards)

    return "".join(backwards)
    # return separate
    # check


print(reverseString(name))
