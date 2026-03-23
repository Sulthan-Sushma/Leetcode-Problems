class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = {}
        for i,j in enumerate(nums):
            complement = target - j
            if complement in l:
                return [l[complement],i]
            l[j] = i
        return []