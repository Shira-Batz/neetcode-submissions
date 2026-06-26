class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anograms = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            anograms[sorted_s].append(s)

        ret = [arr for arr in anograms.values()]
        return ret
        