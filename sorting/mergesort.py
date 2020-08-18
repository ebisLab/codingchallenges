"""
o(n log n)
divide and conquer ---> merge sort and quick sort , (recursion)-->log of n better than o(n^2)  --> saves time
one of the most efficient ways to sort a list
stable
"""
array = [99, 44, 6, 2, 1, 5, 63, 87, 283, 40]


def experiment(array):
    mid = len(array)//2
    l = array[:mid]
    r = array[mid:]
    print(l)
    print(r)
    print(mid)
    print(experiment(l))


count = 0


def mergeSort(array):
    # get the length of the array and divide by 2 o(1)
    # compare their local list to each other
    if len(array) == 1:
        return array
    # else
    else:
        mid = len(array)//2
        left_arr = array[:mid]
        right_arr = array[mid:]
        print("left:", left_arr)
        print("right", right_arr)
        return merge(mergeSort(left_arr), mergeSort(right_arr))


def merge(left, right):
    l = len(left)
    r = len(right)
    leftindex = 0
    rightindex = 0
    sorted_arr = []

    while leftindex < l and rightindex < r:
        global count
        count += 1
        if left[leftindex] < right[right]:
            sorted_arr.append(left[leftindex])
            leftindex += 1
        else:
            sorted_arr.append(right[rightindex])
            rightindex += 1
    return sorted_arr+left[leftindex]+right[rightindex:]


# print(mergeSort(array))
print("EXPERIMENT", experiment(array))
