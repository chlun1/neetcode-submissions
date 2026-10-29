class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        res = 0

        while True:
            stack = []
            for c in s:
                if x > y:
                    if c == "b" and stack and stack[-1] == "a":
                        stack.pop()
                        res += x
                    else:
                        stack.append(c)
                else:
                    if c == "a" and stack and stack[-1] == "b":
                        stack.pop()
                        res += y
                    else:
                        stack.append(c)

            new_stack = []
            for c in stack:
                if c == "b" and new_stack and new_stack[-1] == "a":
                    new_stack.pop()
                    res += x
                elif c == "a" and new_stack and new_stack[-1] == "b":
                    new_stack.pop()
                    res += y
                else:
                    new_stack.append(c)

            if not new_stack or len(new_stack) == len(stack):
                break

            s = "".join(new_stack)

        return res



            

