class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        print("nums", nums, "target", target)
        print("enumarting", list(enumerate(nums)))

        for i, v in enumerate(nums):
            result = target - v
            print("i", i)
            print("v", v)
            print("result", result)
            if result in cache:
                return [cache[result], i]
            cache[v] = i
            print("cache", cache)
        return []
