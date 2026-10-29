from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        counts = Counter(t)
        required = len(counts)
        left = 0
        formed = 0
        res = None

        for right in range(len(s)):
            char = s[right]
            if char in counts:
                counts[char] -= 1
                if counts[char] == 0:
                    formed += 1
            
            while formed == required:
                if res is None or right - left + 1 < len(res):
                    res = s[left: right + 1]

                char = s[left]
                if char in counts:
                    counts[char] += 1
                    if counts[char] > 0:
                        formed -= 1

                left += 1

        return res if res else ""
        