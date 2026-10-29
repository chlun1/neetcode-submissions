from collections import defaultdict


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniques = set(nums)
        res = 0
        for num in uniques:
            if num - 1 not in uniques:
                length = 0
                while num in uniques:
                    length += 1
                    num += 1
                res = max(res, length)
    
        return res
