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
                
                num = 0
                base = 1
                while stack and stack[-1].isdigit():
                    num += base * int(stack.pop())
                    base *= 10

                stack.append(num * "".join(parts[::-1]))
            else:
                stack.append(c)

        return "".join(stack)
