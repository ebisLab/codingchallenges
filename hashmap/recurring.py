arr1 = [5, 2, 3, 4, 2, 6]


def getRecurr(arr):
    combined = []
    for i in arr:
        print(i)
        if i not in combined:
            # print("yes")
            combined.append(i)
        else:
            #     break
            # print("not")
            combined[i] = True  # assign the index in question as True
    return None


print(getRecurr(arr1))


def getRecurr2(arr):
    combined = dict()
    print("combined -->", combined)
    for i in arr:
        # print(i)
        if i in combined:
            # print("yes")
            print("dictionary", combined)
            return i
        else:
            #     break
            # print("not")
            combined[i] = True  # assign the index in question as True

    print("combined-->", combined)
    return None


print(getRecurr2(arr1))
