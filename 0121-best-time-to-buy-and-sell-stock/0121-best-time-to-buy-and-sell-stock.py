class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        Bprice = prices[0]
        profit = 0

        for i in range(len(prices)):
            if prices[i] <= Bprice:
                Bprice = prices[i]
            else:
                currprofit = prices[i] - Bprice
                profit = max(currprofit,profit)
        return profit 
