class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        res = 0

        for i, c in enumerate(s):
            if c == "I":
                if i < n - 1 and s[i + 1] in ("V", "X"):
                    res -= 1
                else:
                    res += 1
            elif c == "X":
                if i < n - 1 and s[i + 1] in ("L", "C"):
                    res -= 10
                else:
                    res += 10
            elif c == "C":
                if i < n - 1 and s[i + 1] in ("D", "M"):
                    res -= 100
                else:
                    res += 100
            elif c == "V":
                res += 5
            elif c == "L":
                res += 50
            elif c == "D":
                res += 500
            elif c == "M":
                res += 1000

        return res
        