'''
Input: a List of integers
Returns: a List of integers
'''


def product_of_all_other_numbers(arr):
    # Your code here

    n = len(arr)
    left = [0]*n
    right = [0]*n
    # left[i] stores prod of all el in sublist [0.. i-1]
    left[0] = 1  # assign the first el as 1, bc it was None
    for i in range(1, len(arr)):
        left[i] = arr[i-1]*left[i-1]
    # right[i] stores prod of el in [i+1.. n-1]
    right[n-1] = 1
    for i in reversed(range(n-1)):
        right[i] = arr[i+1]*right[i+1]
    print(left)
    print(right)

    # replace each el w prod of its left and right sublist
    for i in range(n):
        arr[i] = left[i]*right[i]
    return arr


def product_of_all_other_numbers_RECURSIVE(arr, n, left=1, i=0):

    if i == n:  # base case, no el left on right side
        return 1

    curr = arr[i]  # copy current el

    # calculate prod of right sublist
    right = product_of_all_other_numbers_RECURSIVE(arr, n, left*arr[i], i+1)

    # replace curr el with prod of left and right sublist
    arr[i] = left*right

    # return prod of right sublist including curr el
    return curr * right


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [9, 90]
    arr = [1, 2, 3, 4, 5]
    arr2 = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
            9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")

    print(
        f"Output of product_of_all_other_numbers RECURSIVELY: {product_of_all_other_numbers_RECURSIVE(arr2, len(arr2))}")
