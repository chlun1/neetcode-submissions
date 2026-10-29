from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.n = n
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

    def components(self):
        comps = defaultdict(list)
        for i in range(self.n):
            p = self.find(i)
            comps[p].append(i)

        return list(comps.values())

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        accounts = [
            (x[0], set(x[1:]))
            for x in accounts
        ]

        edges = []
        for i in range(len(accounts)):
            emails_i = accounts[i][1]
            for j in range(i + 1, len(accounts)):
                emails_j = accounts[j][1]
                if emails_i.intersection(emails_j):
                    edges.append((i, j))

        uf = UnionFind(len(accounts))

        for u, v in edges:
            uf.union(u, v)

        res = []
        for comp in uf.components():
            emails = set()
            for i in comp:
                emails |= accounts[i][1]
            res.append([accounts[i][0]] + sorted(list(emails)))

        return res
