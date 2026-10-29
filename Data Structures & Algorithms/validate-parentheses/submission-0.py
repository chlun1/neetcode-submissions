class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in {"(", "{", "["}:
                stack.append(c)
            else:
                if not stack:
                    return False
                
                last = stack.pop()
                if not (
                    (last == "(" and c == ")") or
                    (last == "[" and c == "]") or
                    (last == "{" and c == "}")
                ):
                    return False

        return len(stack) == 0
        