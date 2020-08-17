array = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
# array = [5, 9, 3, 10, 45, 2, 0]
"""Worst and avg case is O(n^2), best is 0(n)"""


def bublSort(array):
    # count = 0

    # -1 because when only 1 item will be left, we don't need to sort that
    for i in range(len(array)-1):
        print(array)
        # In every iteration of the outer loop, one number gets sorted. So the inner loop will run only for the unsorted part
        for j in range(len(array)-i-1):
            # count += 1
            curr = array[j]
            right = array[j+1]
            if curr > right:
                array[j], array[j+1] = array[j+1], array[j]
    return (f"{array} \nNumber of ")


print(bublSort(array))
# print(numbs)
