class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(0, n):
            for j in range(i + 1, n):
                if(nums[i] + nums[j] == target):
                    ret = [i,j]
                    ret.sort()
                    return ret
        return []