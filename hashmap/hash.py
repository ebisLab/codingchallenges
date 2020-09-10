words = ["apple", "book", "cat"]


def my_hash(s, limit):
    str_utf = s.encode()
    total = 0
    for char in str_utf:
        total += char
        # we want to make sure it doesnt exceed a 32 bit num
        # do a binary operator for a bitwise
        total &= 0xffffffff  # ampersandd works on binary

    print('total', total)

    return total % limit


# print(my_hash('card', 8))
# print(my_hash('apple', 8))

hash_tbl = [None]*8  # this will be a power of 2

# ASCII ways to add chars to numbers

# ways to add items to hash_tbl
# use number as index
index = my_hash("hello", len(hash_tbl))
print("index->", index)  # so now it goes in the 4 index
hash_tbl[index] = "Value for Hello"

index = my_hash("world", len(hash_tbl))
print("hashtbl ->", len(hash_tbl))
print("index->", index)  # so now it goes in the 4 index
hash_tbl[index] = "Value for World"

print(hash_tbl)

# * so far o(1) was used ^^^


#! HOW TO READ FROM HASHTBL
# lets retrieve the val for hello
index = my_hash("hello", len(hash_tbl))
print(hash_tbl[index])
