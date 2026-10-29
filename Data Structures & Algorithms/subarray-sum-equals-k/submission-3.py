from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        cur_sum = 0
        comp = defaultdict(int)
        comp[cur_sum] += 1

        for num in nums:
            cur_sum = cur_sum + num
            res += comp[cur_sum - k]
            comp[cur_sum] += 1

        return res
