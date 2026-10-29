class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(curr, counter):
            if len(curr) == n * 2:
                if counter == 0:
                    res.append("".join(curr))
                return

            if not (0 <= counter <= n):
                return

            curr.append("(")
            backtrack(curr, counter + 1)
            curr.pop()
            curr.append(")")
            backtrack(curr, counter - 1)
            curr.pop()
            
        backtrack([], 0)

        return res
        