class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_len = 0
        letters = set()

        for end, char in enumerate(s):
            while char in letters:
                letters.remove(s[start])
                start+=1
            
            letters.add(char)
            current_len = end - start + 1
            
            if current_len > max_len:
                max_len = current_len
            
        return max_len