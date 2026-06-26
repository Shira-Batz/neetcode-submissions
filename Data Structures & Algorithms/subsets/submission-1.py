class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        sub =[]
        
        def dfs(i):
            print(sub, "  ", i)
            if i >= len(nums):
                ret.append(sub.copy())
                return

            sub.append(nums[i])
            dfs(i+1)

            sub.pop()
            dfs(i+1)
            
        dfs(0)
        return ret