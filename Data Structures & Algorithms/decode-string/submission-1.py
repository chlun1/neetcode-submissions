class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c == "]":
                parts = []
                while True:
                    part = stack.pop()
                    if part == "[":
                        break
                    parts.append(part)
                
                num = []
                while stack and stack[-1].isdigit():
                    num.append(stack.pop())
                num = int("".join(num[::-1]))

                stack.append(num * "".join(parts[::-1]))
            else:
                stack.append(c)

        return "".join(stack)
