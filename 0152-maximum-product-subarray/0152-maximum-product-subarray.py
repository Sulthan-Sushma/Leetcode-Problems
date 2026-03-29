class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l,r,res,n = 1,1,nums[0],len(nums)

        for i in range(n):
            l = 1 if l == 0 else l
            r = 1 if r == 0 else r

            l *= nums[i]
            r *= nums[n - 1 - i]

            res = max(res,max(l,r))
        
        return res


