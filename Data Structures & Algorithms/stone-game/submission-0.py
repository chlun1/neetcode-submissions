class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        total = sum(piles)
        cache = {}

        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in cache:
                return cache[(l, r)]
            
            alices_turn = (r - l) % 2
            left = piles[l] * alices_turn
            right = piles[r] * alices_turn

            res = max(
                dfs(l + 1, r) + left,
                dfs(l, r - 1) + right
            )
            cache[(l, r)] = res
            
            return res

        alice_max = dfs(0, len(piles) - 1)

        return alice_max > (total - alice_max)
