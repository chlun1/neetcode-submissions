class Solution:
    def isHappy(self, n: int) -> bool:
        def helper(n):
            res = 0
            while n > 0:
                digit = n % 10
                res += digit ** 2
                n = n // 10
            
            return res

        slow = n
        fast = helper(n)

        while slow != fast:
            slow = helper(slow)
            fast = helper(helper(fast))

        return fast == 1
        