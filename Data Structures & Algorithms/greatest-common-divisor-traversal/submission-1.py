class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [1] * n
        self.n_components = n

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

            self.n_components -= 1
            return True
        return False


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        uf = UnionFind(len(nums))

        factor_index = {}
        for i, num in enumerate(nums):
            f = 2
            while f * f <= num:
                if num % f == 0:
                    if (fi := factor_index.get(f)) is not None:
                        uf.union(fi, i)
                    else:
                        factor_index[f] = i

                    while num % f == 0:
                        num = num // f
                f += 1 

            if num > 1:
                if (fi := factor_index.get(num)) is not None:
                    uf.union(fi, i)
                else:
                    factor_index[num] = i

        return uf.n_components == 1
        