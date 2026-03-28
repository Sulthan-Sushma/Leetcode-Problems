class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = -10000
        temp = 0
        for i in range(len(nums)):
            temp+=nums[i]
            total = max(total, temp)
            temp = max(temp,0)
        return total