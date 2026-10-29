class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # Optimisation: try longer sticks first and prune earlier.
        matchsticks.sort(reverse=True)

        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        
        target = total // 4

        def backtrack(start, sides):
            if start == len(matchsticks):
                return all(x == target for x in sides)

            matchstick = matchsticks[start]

            for i in range(4):
                # Optimisation: if side[i - 1] didn't work and side[i] == side[i - 1]
                # then side[i] wouldn't work either so skip it.
                if i > 0 and sides[i] == sides[i - 1]:
                    continue

                sides[i] += matchstick
                if sides[i] <= target and backtrack(start + 1, sides):
                    return True
                sides[i] -= matchstick

                # Optimisation: if we fail to place a stick in an empty side, 
                # it won't work in any subsequent empty side.
                if sides[i] == 0:
                    break

            return False

        return backtrack(0, [0, 0, 0, 0])
