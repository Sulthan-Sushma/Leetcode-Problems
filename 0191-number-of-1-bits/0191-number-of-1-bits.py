class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            count += n & 1   # check last bit
            n = n >> 1       # shift right
        return count