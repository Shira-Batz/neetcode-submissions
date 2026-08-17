class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        int xors = 0;
        vector<int> res;
        for (int i = 0; i < nums.size(); i++) {
            xors = xors ^ nums[i];
        }
        int diff = 1;
        while ((xors & diff) == 0) {
            diff <<= 1;
        }
        int a = 0, b = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] & diff) {
                a = a ^ nums[i];
            }
            else {
                b = b ^ nums[i];
            }
        }
        return {a, b};
    }
};