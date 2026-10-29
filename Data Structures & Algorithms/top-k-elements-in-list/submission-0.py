from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        freq = [[] for _ in range(max(counts.values()) + 1)]
        for num, count in counts.items():
            freq[count].append(num)
        
        res = []
        for num in reversed(freq):
            if len(num) == 0:
                continue
            res.extend(num)
            if len(res) >= k:
                return res[:k]
        