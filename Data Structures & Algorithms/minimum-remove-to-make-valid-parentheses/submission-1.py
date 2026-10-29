class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        res = []

        for c in s:
            if c == "(":
                stack.append(len(res))
                res.append(c)
            elif c == ")":
                if stack:
                    stack.pop()
                    res.append(c)
            else:
                res.append(c)

        to_delete = set(stack)

        return "".join((c for i, c in enumerate(res) if i not in to_delete))
        