class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L,H = 0,len(nums) - 1

        while L <= H:
            M =  (L + H)//2
            
            if nums[M] == target:
                return M
            if nums[L] <= nums[M]:
                if target >= nums[L] and target < nums[M]:
                    H = M - 1
                else:
                    L = M + 1
            else:
                if target <= nums[H] and target > nums[M]:
                    L = M + 1
                else:
                    H = M - 1 
        return -1