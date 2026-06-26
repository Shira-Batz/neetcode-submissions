class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidates = defaultdict(int)
        for num in nums:
            candidates[num] += 1

            if len(candidates) <= 2:
                continue

            new_candidates = defaultdict(int)
            for (num, c) in candidates.items():
                if candidates[num] > 1:
                    new_candidates[num] = c - 1
            candidates = new_candidates

        res = []
        for num in candidates:
            if nums.count(num) > len(nums) // 3:
                res.append(num)

        return res