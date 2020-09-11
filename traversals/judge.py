def findjudge(n, trust):
    trust_table = []

    # hashmap ?
    # hash table?
    # what if the n is 1? should it return 1
    for i in range(n+1):
        trust_table.append(0)

    if n == 1:  # if n is 1, then return 1
        return 1
    for i, j in trust:
        # decrease point from i if j trusts
        trust_table[i] -= 1
        # increase point in j if others trust j
        trust_table[j] += 1

    for i in range(1, n+1):
        if trust_table[i] == n-1:  # spy trusted by n-1 people, spy trusts no one
            return i
    print(trust_table)
    return -1
