hash_tbl = [None]*8  # <- 8 slots init to None


def my_hash(s):
    # take every char in string, and convert char to num
    # convert each char into UTF-8 numbers

    string_utf = s.encode()

    total = 0
    for char in string_utf:
        total += char
        total &= 0xffffffff  # limiting to 32 bits
    return total


def hash_index(key):
    hash_num = my_hash(key)
    return hash_num % len(hash_tbl)


def put(key, val):
    # hash the key and get an index
    i = hash_index(key)
    # find the start of the linked list using the index
    # search thorugh ll for key

    # insert into this liked list a new Hashtable Entry
    # if the key already exists in the ll
    # replace the value
    # else
    # add new hashtable entry to the head of linked list

    # CHECK IF SOMETHING ALREADY EXISTS AT THE INDEX
    if hash_tbl[i] is not None:
        print(f"Collision Overwriting {repr(hash_tbl[i])}!")
    # Store the value in the array at the hashed index
    hash_tbl[i] = val


def get(key):
    # hash the key and get an index
    i = hash_index(key)
    # return the value from the array at the index
    return hash_tbl[i]


put("hello", "hello value")
put("world", "world value")

print(hash_tbl)

print("foo", "Foo VALUE")
print(hash_tbl)

value = get("foo")
print(value)

print(hash_index("hello"))
print(hash_index("food"))
