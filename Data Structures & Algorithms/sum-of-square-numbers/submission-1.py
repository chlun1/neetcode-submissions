class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        c_sqrt = int(c ** 0.5) + 1

        for a in range(c_sqrt):
            target = (c - a ** 2) ** 0.5
            if int(target) == target:
                return True

        return False
