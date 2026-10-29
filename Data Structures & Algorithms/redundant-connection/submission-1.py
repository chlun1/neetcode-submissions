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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges) + 1)

        for u, v in edges:
            if not uf.union(u, v):
                # Can just return the first redundant edge since
                # there's just one redundant edge and the ones that
                # came before can't be redundant.
                return [u, v]
