class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [1] * n

    def find(self, u):
        if self.parents[u] != u:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)

        if pu != pv:
            if self.ranks[pu] >= self.ranks[pv]:
                self.parents[pv] = pu
                self.ranks[pu] += self.ranks[pv]
            else:
                self.parents[pu] = pv
                self.ranks[pv] += self.ranks[pu]
            return True

        return False


def mst(edges, n, uf, edges_added):
    edges.sort(key=lambda x: x[2])
    weight = 0

    for u, v, w in edges:
        if uf.union(u, v):
            weight += w
            edges_added += 1

            if edges_added == n - 1:
                return weight

    return -1


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        uf = UnionFind(n)
        base_weight = mst(edges.copy(), n, uf, 0)
        critical = []
        pseudo = []

        for i, edge in enumerate(edges):
            uf = UnionFind(n)
            weight = mst(edges[:i] + edges[i + 1:], n, uf, 0)

            if weight > base_weight or weight == -1:
                critical.append(i)
            else:
                uf = UnionFind(n)
                u, v, w = edge
                uf.union(u, v)
                weight = w + mst(edges[:i] + edges[i + 1:], n, uf, 1)
    
                if weight == base_weight:
                    pseudo.append(i)

        return [critical, pseudo]
        