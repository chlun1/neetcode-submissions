class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []

        def backtrack(curr):
            if len(res) == k:
                return

            if len(curr) == n:
                res.append("".join(curr))
                return

            for c in ["a", "b", "c"]:
                if curr and c == curr[-1]:
                    continue
                
                curr.append(c)
                backtrack(curr)
                curr.pop()
            
        backtrack([])

        return res[k - 1] if len(res) >= k else ""
