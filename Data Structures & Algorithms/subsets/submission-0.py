class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        self.addSub(nums, [], ret)
        return ret
    
    def addSub(self, nums: List[int], sub: List[int], ret: List[List[int]]):
        if nums:
            curr_nums = nums.copy()
            n = curr_nums.pop(0)
            without_n = sub.copy()
            with_n = sub.copy()
            with_n.append(n)
            
            self.addSub(curr_nums, without_n, ret)
            self.addSub(curr_nums, with_n, ret)

        else:
            ret.append(sub)