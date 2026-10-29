class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c2idx = {}
        l = 0
        res = 0
        for r in range(len(s)):
            c = s[r]
            if (idx := c2idx.get(c, -1)) >= l:
                l = idx + 1
            c2idx[c] = r
            res = max(res, r - l + 1)
    
        return res
        