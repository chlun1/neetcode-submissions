from collections import defaultdict


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1

        i = 0
        for num, count in counts.items():
            for _ in range(min(2, count)):
                nums[i] = num
                i += 1

        return i
        