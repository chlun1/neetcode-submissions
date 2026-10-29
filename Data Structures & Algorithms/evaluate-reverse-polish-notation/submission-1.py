class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            if s in {"+", "-", "*", "/"}:
                num2 = stack.pop()
                num1 = stack.pop()
                if s == "+":
                    stack.append(num1 + num2)
                elif s == "-":
                    stack.append(num1 - num2)
                elif s == "*":
                    stack.append(num1 * num2)
                else:
                    stack.append(int(num1 / num2))
            else:
                if s[0] == "-":
                    num = -1 * int(s[1:])
                else:
                    num = int(s)
                stack.append(num)

        return stack[-1]
