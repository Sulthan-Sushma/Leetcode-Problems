class Solution {
public:
    int search(vector<int>& nums, int target) {
        int L = 0;
        int H = nums.size() - 1;
        
        while(L <= H){
            int M = (L + H)/2;

            if(nums[M] == target){
                return M;
            }

            if (nums[L] <= nums[M]){
                if(target >= nums[L] && target < nums[M]){
                    H = M - 1;
                }
                else{
                    L = M + 1;
                }
            }

            else{
                if(target <= nums[H] && target > nums[M]){
                    L = M + 1;
                }
                else{
                    H = M - 1;
                }
            }
        }

        return -1;
    }
};