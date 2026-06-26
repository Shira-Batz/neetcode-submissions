class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = max(1, ((sum(piles) - 1) // h) + 1)
        r = max(piles)
        mid: int
        while l <= r:
            sum_hours = 0
            mid = (l+r)//2
            for b in piles:
                sum_hours += (b + mid - 1) // mid
            print(mid," ", sum_hours)
            if sum_hours <= h:
                r = mid - 1
            elif sum_hours > h:
                l = mid + 1
        return l