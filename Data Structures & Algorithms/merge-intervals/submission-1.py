class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        curr_start, curr_end = -1, -1
        ret = []

        for i, p in enumerate(intervals):
            start, end = p
            if start <= curr_end:
                if end > curr_end:
                    curr_end = end
            else:
                if curr_start > -1:
                    ret.append([curr_start, curr_end])
                curr_start = start
                curr_end = end
        if curr_start > -1:
            ret.append([curr_start, curr_end])
        return ret
