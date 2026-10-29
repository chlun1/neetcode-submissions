class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        j = 0

        for i in range(len(s)):
            while j < len(t) and s[i] != t[j]:
                j += 1

            if j == len(t):
                return False
                
            j += 1

        return True
        