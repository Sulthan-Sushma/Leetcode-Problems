class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        if nums is None or len(nums) < 3:
            return []

        nums.sort()
        hs = set()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            p1, p2 = i + 1, len(nums) - 1

            while p1 < p2:
                S = nums[i] + nums[p1] + nums[p2]

                if S == 0:
                    hs.add((nums[i], nums[p1], nums[p2]))

                    while p1 < p2 and nums[p1] == nums[p1 + 1]:
                        p1 += 1
                    while p1 < p2 and nums[p2] == nums[p2 - 1]:
                        p2 -= 1

                    p1 += 1
                    p2 -= 1

                elif S < 0:
                    p1 += 1
                else:
                    p2 -= 1

        return [list(x) for x in hs]