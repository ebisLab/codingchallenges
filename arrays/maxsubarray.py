
import time
start_time = time.time()


def brute(arr):
    max_ = 0
    if len(arr) == 0:
        return None
    for i in range(len(arr)):
        sum_ = 0
        for j in range(i, len(arr)):
            sum_ += arr[j]
            max_ = max(max_, sum_)
        return max_


array_nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(brute(array_nums))
print("--- %s seconds ---" % (time.time() - start_time))


def faster(arr):
    max_ = maxarray = arr[0]
    for i in range(1, len(arr)):
        maxarray = max(arr[i], maxarray+arr[i])
        max_ = max(maxarray, max_)
    return max_


array_nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(faster(array_nums))
print("--- %s seconds ---" % (time.time() - start_time))
