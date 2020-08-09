
import time
start_time = time.time()
# // Given 2 arrays, create a function that let's a user know (true/false) whether these two arrays contain any common items
# //For Example:
# //const array1 = ['a', 'b', 'c', 'x'];//const array2 = ['z', 'y', 'i'];
# //should return false.
# //-----------
# //const array1 = ['a', 'b', 'c', 'x'];//const array2 = ['z', 'y', 'x'];
# //should return true.

# // 2 parameters - arrays - no size limit - the array can get very large
# // return true or false


arr1 = ['a', 'b', 'c', 'x']
arr2 = ['z', 'y', 'i', 'a']


def containsCommon2(arr1, arr2):
    map_ = dict()

    # for i in range(len(arr1)):
    #     map_[arr1[i]] = True
    for i in range(len(arr1)):
        map_[arr1[i]] = True

    for i in range(len(arr2)):
        if arr2[i] in map_:
            return True

    return False


print(containsCommon2(arr1, arr2))
print("--- %s seconds ---" % (time.time() - start_time))
