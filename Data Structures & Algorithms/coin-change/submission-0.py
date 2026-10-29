class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def helper(amount):
            if amount < 0:
                return -1
            if amount == 0:
                return 0
            
            if amount in cache:
                return cache[amount]

            res = float("inf")
            
            for coin in coins:
                if (tmp := helper(amount - coin)) != -1:
                    res = min(res, tmp + 1)

            cache[amount] = res if res < float("inf") else -1

            return cache[amount]
                
        return helper(amount)
        