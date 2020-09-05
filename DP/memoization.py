"""caching helps speed up data

MEMOIZATION - specific form of caching that involves caching the return value of func based on its paramaters, and if paramater doesnt change, then its memoized, it uses the cache version 
"""

# without MEMOIZATION


def addTo80(n):
    print("long time")
    return n + 80


print(addTo80(5))
print(addTo80(5))
print(addTo80(5))

# optimize this
cache = {}
# cache ={
# 5:85
# }


def memoizedAddTo80(n):
    if n in cache:
        return cache[n]
    else:
        print("long time")
        cache[n] = n+80
        return cache[n]


print("1", memoizedAddTo80(5))
print("2", memoizedAddTo80(5))
print("2", memoizedAddTo80(5))


# IDEALLY is good to put the cache inside of the function as opposed to global scope
# cache gets reset every run

def memoizedInsideAddTo80():
    cache = {}

    def memoized(n):
        if n in cache:
            return cache[n]
        else:
            print("long time")
            cache[n] = n+80
            return cache[n]
    return memoized


memoized = memoizedInsideAddTo80()

print("memoized", memoized(7))
print("memoized", memoized(6))


# print("1", memoizedInsideAddTo80(5))
# print("2", memoizedInsideAddTo80(5))
# print("2", memoizedInsideAddTo80(5))
