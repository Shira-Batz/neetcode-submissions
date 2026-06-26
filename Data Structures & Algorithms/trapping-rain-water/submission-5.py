class Solution:
    def trap(self, height: List[int]) -> int:
        sum_water = 0
        holes = []
        start = 0
        curr_max_i = 0
        i = 0
        while i < len(height):
            if height[i] >= height[start] > 0:
                holes.append((start, i))
                start = i
                curr_max_i = i + 1
            elif start == 0 and height[start] == 0 and height[i] > 0:
                start = i
                curr_max_i = i + 1
            elif height[curr_max_i] < height[i]:
                curr_max_i = i
            if i == len(height) - 1 and height[min(curr_max_i, len(height)-1)] < height[start]:
                i = curr_max_i
                holes.append((start, i))
                start = i
                curr_max_i = i + 1
            i+=1
        for hole in holes:
            l = hole[0] + 1
            r = hole[1] - 1
            h = min(height[hole[0]], height[hole[1]])
            for i in range (l, r + 1):
                sum_water += h - height[i]
        print(holes)
        return sum_water