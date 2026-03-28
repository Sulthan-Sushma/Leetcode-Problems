class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int total = -10000;
        int temp = 0;
        int n = nums.size();
        for(int i = 0;i<n;i++){
            temp = temp + nums[i];
            total = max(total,temp);
            temp = max(temp,0);
        }
        return total;
    }
};