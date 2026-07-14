class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            t = target - n
            if t in d:
                return [d[t], i]
            else:
                d[n] = i
