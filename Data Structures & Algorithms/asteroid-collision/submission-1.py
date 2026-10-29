class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for x in asteroids:
            if not stack or x > 0:
                stack.append(x)
            elif x < 0:
                while stack and stack[-1] > 0:
                    top = stack[-1]
                    if top > -x:
                        x = None
                        break
                    elif top == -x:
                        x = None
                        stack.pop()
                        break
                    else:
                        stack.pop()
                if x:
                    stack.append(x)

        return stack
        