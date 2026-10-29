from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        l = 0
        res = 0
        for r in range(len(s)):
            freq[s[r]] += 1
            max_freq = max(freq.values())
            while r - l - max_freq + 1 > k:
                freq[s[l]] -= 1
                max_freq = max(freq.values())
                l += 1
            res = max(res, r - l + 1)

        return res
        