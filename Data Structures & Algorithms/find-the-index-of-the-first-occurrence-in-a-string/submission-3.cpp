class Solution {
public:
    int strStr(string haystack, string needle) {
        int n = haystack.length(), m = needle.length();
        for (int j = 0; j <= n - m; j++) {
            if (haystack.substr(j, m) == needle) return j;
        }
        return -1;
    }
};