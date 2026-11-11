class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        asc = [[0] * 4 for _ in range(n)]
        des = [[0] * 4 for _ in range(n)]

        for i in range(n):
            asc[i][1] = 1
            des[i][1] = 1

        for count in range(2, 4):
            for i in range(n):
                for j in range(i + 1, n):
                    if rating[i] < rating[j]:
                        asc[i][count] += asc[j][count - 1]
                    if rating[i] > rating[j]:
                        des[i][count] += des[j][count - 1]

        res = 0
        for i in range(n):
            res += asc[i][count] + des[i][count]

        return res
