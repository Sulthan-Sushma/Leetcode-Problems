class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int n = nums.size();
        int l = 1;
        int r = 1;
        int res = nums[0];

        for(int i = 0;i < n;i++){
            l = l == 0 ? 1 : l;
            r = r == 0 ? 1 : r;

            l = l * nums[i];
            r = r * nums[n - 1 - i];

            res = max(res,max(l,r));
        }
        return res;
    }
};