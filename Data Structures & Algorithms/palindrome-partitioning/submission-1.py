class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_pali(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1

            return True

        def backtrack(start, curr):
            if start == len(s):
                res.append(curr.copy())

            for i in range(start, len(s)):
                if is_pali(start, i):
                    curr.append(s[start: i + 1])
                    backtrack(i + 1, curr)
                    curr.pop()

        backtrack(0, [])

        return res
   