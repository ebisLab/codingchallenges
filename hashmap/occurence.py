import time

arr1 = "AABAACAADAABAABA"


def wordcount(arr):
    t0 = time.time()
    countme = dict()
    for i in arr:
        print("count", i)
        countme[i] = countme.get(i, 0)+1
        # countme[i] = count
    t1 = time.time()
    print(f"The search took {t1-t0} seconds.")

    return countme


print(wordcount(arr1))


large1 = ['nemo' for i in range(5)]
print(large1)
