a1 = [0, 3, 4, 31]
a2 = [4, 6, 30]


def mergeArr(arr1, arr2):

    combined = []

    for i in arr1:
        combined.append(i)

    for i in arr2:
        combined.append(i)

    combined.sort()

    return combined


print(mergeArr(a1, a2))
