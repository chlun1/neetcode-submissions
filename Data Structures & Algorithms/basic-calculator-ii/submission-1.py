class Solution:
    def calculate(self, s: str) -> int:
        i = 0
        stack = []
        res = 0

        while i < len(s):
            if s[i] in {"+", "-", "*", "/"}:
                stack.append(s[i])
                i += 1
            elif s[i].isspace():
                i += 1
            else:
                num = 0
                while i < len(s) and s[i].isdigit():
                    num *= 10
                    num += int(s[i])
                    i += 1

                if stack and stack[-1] in {"*", "/"}:
                    op = stack.pop()
                    num2 = stack.pop()
                    if op == "*":
                        stack.append(num * num2)
                    else:
                        stack.append(int(num2 / num))
                else:
                    stack.append(num)

        if stack:
            res += stack[0]

        op = "+"

        for x in stack[1:]:
            if x in {"+", "-"}:
                op = x
            elif op == "+":
                res += x
            else:
                res -= x

        return res
        