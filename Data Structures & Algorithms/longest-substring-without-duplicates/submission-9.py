class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        start = 0
        max = 0
        letters = set()

        for index, char in enumerate(s):
            if (not char in letters):
                letters.add(char)
                count+=1

            else:
                for k in range(start, index):
                    if char == s[k]:
                        start = k+1
                        break
                    letters.remove(s[k])
                    count-=1

            if (count > max):
                    max = count
        
        return max
        