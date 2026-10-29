class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        cache = {}

        def dfs(i, M, alice_turn):
            if i == len(piles):
                return 0
            if (i, M, alice_turn) in cache:
                return cache[(i, M, alice_turn)]

            res = 0 if alice_turn else float("inf")
            stones = 0

            for j in range(i, min(i + (2 * M), len(piles))):
                stones += piles[j] * alice_turn
                func = max if alice_turn else min
                res = func(
                    res,
                    dfs(j + 1, max(M, j - i + 1), not alice_turn) + stones
                )

            cache[(i, M, alice_turn)] = res

            return res

        return dfs(0, 1, True)
        