class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [1] * n

    def find(self, u):
        if self.parents[u] != u:
            self.parents[u] = self.find(self.parents[u])

        return self.parents[u]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu != pv:
            if self.ranks[pu] >= self.ranks[pv]:
                self.parents[pv] = pu
                self.ranks[pu] += self.ranks[pv]
            else:
                self.parents[pu] = pv
                self.ranks[pv] += self.ranks[pu]
            
            return True

        return False


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []

        for i in range(n):
            u = points[i]
            for j in range(i + 1, n):
                v = points[j]
                dist = abs(u[0] - v[0]) + abs(u[1] - v[1])
                edges.append((dist, i, j))

        edges.sort(key=lambda x: x[0])

        uf = UnionFind(n)
        cost = 0
        joined = 0

        for dist, i, j in edges:
            if uf.union(i, j):
                cost += dist
                joined += 1

                if joined == n - 1:
                    break

        return cost
        