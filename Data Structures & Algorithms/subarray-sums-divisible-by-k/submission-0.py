from collections import defaultdict


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        res = 0
        prefix = defaultdict(int)
        prefix[curr_sum] = 1

        for num in nums:
            curr_sum += num
            res += prefix[curr_sum % k]
            prefix[curr_sum % k] += 1

        return res
            