from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = set()
        counts = defaultdict(int)
        thresh = len(nums) // 3
        for num in nums:
            counts[num] += 1
            if counts[num] > thresh:
                res.add(num)
        
        return list(res)
        