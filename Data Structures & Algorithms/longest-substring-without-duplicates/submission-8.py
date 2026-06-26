class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = 0
        start = 0
        max = 0
        letters = [0 for _ in range(256)]

        for index, char in enumerate(s):
            i = ord(char)
            if (letters[i] == 0):
                letters[i]+=1
                c+=1

            else:
                for k in range(start, index):
                    j = ord(s[k])
                    if i == j:
                        start = k+1
                        break
                    letters[j] = 0
                    c-=1

            if (c > max):
                    max = c
        
        return max
        