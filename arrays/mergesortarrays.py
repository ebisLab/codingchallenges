
import time
start_time = time.time()


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
print("--- %s seconds ---" % (time.time() - start_time))


def mergeArr2(arr1, arr2):
    merge_all = []
    arr1item = arr1[0]
    arr2item = arr2[0]
    i = 0
    j = 0

    print(arr1, arr2)

    if len(arr1) == 0 or len(arr2) == 0:
        return arr1+arr2

        #         # if they're both empty

    # while arr1[i] or arr2[j]:
    #     if arr2item or arr1item < arr2item:
    #         merge_all.append(arr1item)
    #         i += 1
    #     else:
    #         merge_all.append(arr2item)
    #         arr2item = arr2[j]
    #         j += 1
    #     return merge_all

    while i < len(arr1) and j < len(arr2):
        print(arr1item, arr2item)
        if arr1[i] <= arr2[i]:
            merge_all.append(arr1[i])
            i += 1
        else:
            merge_all.append(arr2item)
            arr2item = arr2[j]
            j += 1
        return merge_all+arr1[i:]+arr2[j:]


print(mergeArr2(a1, a2))
print("--- %s seconds ---" % (time.time() - start_time))
