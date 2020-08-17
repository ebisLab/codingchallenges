"""
best time to use this times you're pretty sure list is almost sorted
o(n)
worst case(o(n^2))
"""
array = [99, 44, 6, 2, 1, 5, 63, 87, 283, 40]


def insertionSort(array):
    count = 0
    for i in range(1, len(array)):
        first = array[i]
        last = array[i-1]  # store the last element which is sorted
        count += 1
        if first < last:
            for j in range(i-1, -1, -1):  # for every element we find in the sorted part which is greter than the current element, we shift them one place towards right to make room for the current element
                count += 1
                if first < array[j]:
                    if j == 0:  # reach the beginning of array
                        array[j+1] = array[j]
                        array[j] = first
                    else:
                        array[j+1] = array[j]
                else:
                    array[j+1] = first
                    break
    return array


print(insertionSort(array))
