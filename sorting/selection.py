"""o(n^2)--> not very fast, nested for loops, o1 space complexity"""
array = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
# array = [5, 9, 3, 10, 45, 2, 0]


def selection(array):
    count = 0
    for i in range(len(array)):
        # set current index as minum
        minimum = array[i]  # curren
        index = i
        for j in range(i+1, len(array)):
            count += 1
            if array[j] < minimum:
                # update minimum if current is lower that what we had previously
                minimum = array[j]
                index = j
        if index is not i:
            array[index], array[i] = array[i], array[index]
    return array


print(selection(array))
