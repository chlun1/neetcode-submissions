class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def helper(n):
            res = 0
            while n > 0:
                digit = n % 10
                res += digit ** 2
                n = n // 10
            
            return res

        while n != 1:
            n = helper(n)
            if n in seen:
                return False

            seen.add(n)

        return True
        