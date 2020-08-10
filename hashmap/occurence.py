arr1 = "AABAACAADAABAABA"


def wordcount(arr):
    countme = dict()
    for i in arr:
        print("count", i)
        countme[i] = countme.get(i, 0)+1
    return countme


print(wordcount(arr1))
