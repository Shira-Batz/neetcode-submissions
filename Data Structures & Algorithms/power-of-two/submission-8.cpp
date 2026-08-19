class Solution {
public:
    bool isPowerOfTwo(int n) {
        bool ans = (n > 0 && (n & (n - 1)) == 0);
        return ans;
    }
};