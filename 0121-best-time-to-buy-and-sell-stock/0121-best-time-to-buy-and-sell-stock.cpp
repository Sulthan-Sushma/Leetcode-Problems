class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int Bprice = prices[0];
        int profit = 0;
        for (int i = 1;i < prices.size();i++){
            if (prices[i] < Bprice){
                Bprice = prices[i];
            }
            else{
                int currprofit = prices[i] - Bprice;
                profit = max(currprofit,profit);
            }
        }
        return profit;
    }
};