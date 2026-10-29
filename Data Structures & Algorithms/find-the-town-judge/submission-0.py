class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        out_deg = [0] * n
        in_deg = [0] * n
        
        for a, b in trust:
            out_deg[a - 1] += 1
            in_deg[b - 1] += 1

        for i, deg in enumerate(out_deg):
            if deg == 0 and in_deg[i] == n - 1:
                return i + 1

        return -1
        