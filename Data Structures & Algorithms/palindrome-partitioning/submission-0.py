class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(start, curr):
            if start == len(s):
                res.append(curr.copy())

            for i in range(start, len(s)):
                if s[start: i + 1] == s[start: i + 1][::-1]:
                    curr.append(s[start: i + 1])
                    backtrack(i + 1, curr)
                    curr.pop()

        backtrack(0, [])

        return res
   