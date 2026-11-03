class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        return max(sum((x >> i) & 1 for x in candidates) for i in range(32))
