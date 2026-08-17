class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        int xors = 0;
        vector<int> res;
        for (int& num : nums) {
            xors = xors ^ num;
        }
        int diff = xors & (-xors);
        int a = 0, b = 0;
        for (int& num : nums) {
            if (num & diff) {
                a = a ^ num;
            }
            else {
                b = b ^ num;
            }
        }
        return {a, b};
    }
};