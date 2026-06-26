import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = math.ceil(sum(piles)/h)
        r = max(piles)
        mid: int
        while l <= r:
            sum_hours = 0
            mid = (l+r)//2
            for b in piles:
                sum_hours += math.ceil(b/mid)
            print(mid," ", sum_hours)
            if sum_hours <= h:
                r = mid - 1
            elif sum_hours > h:
                l = mid + 1
            else:
                break
        return mid