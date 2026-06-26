class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        l_max, r_max = height[l], height[r]
        sum_water = 0
        
        while l < r:
            if r_max > l_max:
                l+=1
                l_max = max(l_max, height[l])
                sum_water += l_max - height[l]
            else:
                r-=1
                r_max = max(r_max, height[r])
                sum_water += r_max - height[r]
        
        return sum_water