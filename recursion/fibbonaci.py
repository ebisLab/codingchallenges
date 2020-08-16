def fibbonacciIt(n):
    answer1 = 0
    answer2 = 1
    if n == 0:
        return answer1
    if n == 1:
        return answer2
    for i in range(2, n+1):
        answer3 = answer1+answer2
        answer1 = answer2
        answer2 = answer3
    return answer3


def fibonnaciRecursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonnaciRecursive(n-1)+fibonnaciRecursive(n-2)


print(fibonnaciRecursive(7))
print(fibbonacciIt(7))
