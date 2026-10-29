class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in sorted(zip(position, speed), reverse=True)]
        p, s = pairs[0]
        prev_t = (target - p) / s
        res = 1

        for i in range(1, len(pairs)):
            p, s = pairs[i]
            t = (target - p) / s
            if t > prev_t:
                res += 1
                prev_t = t

        return res
