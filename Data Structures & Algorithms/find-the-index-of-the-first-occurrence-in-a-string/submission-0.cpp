class Solution {
public:
    int strStr(string haystack, string needle) {
        int i = -1;
        int k = 0;
        for (int j = 0; j < haystack.length(); j++) {
            if (haystack.at(j) == needle.at(k)) {
                if (i == -1) {
                    i = j;
                }
                k++;
                if (k == needle.length()) {
                    return i;
                }
            }
            else if (i != -1) {
                j = i;
                k = 0;
                i = -1;
            }
        }
        return -1;
    }
};