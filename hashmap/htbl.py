class Hashtable:
    def __init__(self):
        """
        Create an array(self.my dict) w/ a bucket size - derived from load factor.
        Load factor --> a measure that decides when to increase the Hashmap capacity to maintain the get() and put() operator complexity of o(1).
        Default load factor of hashmap is .75f (75% of the map size)
        Load Factor = (n/k)
        n => max number of elements that can be stored
        k => bucket size
        Optimal load factor is (2/3) so that the effect of hash collision is minimum"""
        self.bucket = 16
        self.hashmap = [[] for i in range(self.bucket)]

    def __str__(self):
        return str(self.__dict__)

    def hash(self, key):
        return len(key) % self.bucket

    def put(self, key, value):
        """value may already be present"""
        hash_val = self.hash(key)
        reference = self.hashmap[hash_val]
        for i in range(len(reference)):
            # if reference[i][0] == key:
            #     reference[i][1] = value
            #     return None
            # * === cleaner way to write this ====
            if not reference:
                reference = []
            # * ==========================
        reference.append([key, value])
        return None

    def get(self, key):  # if there's no collision, it can be O(1)
        """return value to which the specified key is mapped, or -1 if this map contains no mapping for the key"""

        hash_val = self.hash(key)
        reference = self.hashmap[hash_val]
        for i in range(len(reference)):
            if reference[i][0] == key:   # grab this first array[i], then 0
                return reference[i][1]  # current bucket and 1 (1000)

        return -1  # <-- undefined

    # iterate and spit out what's in the hash map

    def keys(self):
        keysArr = []

        for i in range(self.bucket):
            if self.hashmap[i] != 0:  # if its empty
                for j in range(len(self.hashmap[i])):
                    keysArr.append(self.hashmap[i][j][0])
        return keysArr


h = Hashtable()
h.put('grapes', 1000)
h.put('apples', 10)
h.put('ora', 300)
print(h.get('grapes'))
print(h)
h.keys()
print(h.keys())
# h.remove('apples')
print(h)
