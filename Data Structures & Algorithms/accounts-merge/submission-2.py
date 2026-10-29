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
        email2acc = {}
        uf = UnionFind(len(accounts))

        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                if email in email2acc:
                    uf.union(i, email2acc[email])
                else:
                    email2acc[email] = i

        email_group = defaultdict(list)
        for e, i in email2acc.items():
            parent = uf.find(i)
            email_group[parent].append(e)

        return [
            [accounts[i][0]] + sorted(emails)
           for i, emails in email_group.items()
        ]
