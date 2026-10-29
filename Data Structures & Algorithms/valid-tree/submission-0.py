class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [0] * n

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
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        uf = UnionFind(n)

        for u, v in edges:
            if not uf.union(u, v):
                return False

        return True
        