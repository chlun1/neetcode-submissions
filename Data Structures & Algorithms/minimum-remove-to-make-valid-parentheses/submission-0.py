class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        res = []

        for c in s:
            if c == "(":
                stack.append((c, len(res)))
                res.append(c)
            elif c == ")":
                if stack and stack[-1][0] == "(":
                    stack.pop()
                    res.append(c)
            else:
                res.append(c)

        to_delete = set(x[1] for x in stack)

        return "".join((c for i, c in enumerate(res) if i not in to_delete))
        