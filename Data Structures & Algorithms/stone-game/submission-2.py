class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        total = sum(piles)
        dp = [[0] * len(piles) for _ in range(len(piles) + 1)]

        for l in range(len(piles) - 1, -1, -1):
            for r in range(l, len(piles)):
                alices_turn = (r - l) % 2
                left = piles[l] * alices_turn
                right = piles[r] * alices_turn
                dp[l][r] = max(dp[l + 1][r] + left, dp[l][r - 1] + right)

        alice_max = dp[0][len(piles) - 1]

        return alice_max > (total - alice_max)
        