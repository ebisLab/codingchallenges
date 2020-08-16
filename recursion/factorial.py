import math


def findFactorialRecurvisve(number):
    if number <= 1:
        return 1
    else:
        return number * findFactorialRecurvisve(number-1)

    # return number*math.factorial(number-1)
    # findFactorialRecurvisve()


def findFactorivalIterative(number):
    answer = 1
    for i in range(1, number+1):
        # print(number*i)
        answer *= i
    return answer


print(findFactorialRecurvisve(5))
print(findFactorivalIterative(5))
