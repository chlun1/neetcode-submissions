class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        cache = {}
        
        def dfs(i, alice):
            if i == len(stoneValue):
                return 0

            if (i, alice) in cache:
                return cache[(i, alice)]

            res = -float("inf") if alice else float("inf")
            score = 0
            func = max if alice else min

            for j in range(3):
                if i + j == len(stoneValue):
                    break

                score += stoneValue[i + j] * alice
                res = func(
                    res,
                    score + dfs(i + j + 1, not alice),
                )

            cache[(i, alice)] = res

            return res

        total = sum(stoneValue)
        alice_score = dfs(0, True)

        if alice_score > total / 2.0:
            return "Alice"
        if alice_score < total / 2.0:
            return "Bob"

        return "Tie"
