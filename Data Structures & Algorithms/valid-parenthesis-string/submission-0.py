class Solution:
    def checkValidString(self, s: str) -> bool:
        left_stack = []
        star_stack = []

        for i, c in enumerate(s):
            if c == "(":
                left_stack.append(i)
            elif c == "*":
                star_stack.append(i)
            else:
                if left_stack:
                    left_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False

        if left_stack:
            while left_stack and star_stack:
                li = left_stack.pop()
                si = star_stack.pop()
                if si < li:
                    return False

        return len(left_stack) == 0
        