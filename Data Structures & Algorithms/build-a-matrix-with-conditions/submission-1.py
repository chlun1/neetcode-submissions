from collections import deque


class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        row_adj = [[] for _ in range(k + 1)]
        col_adj = [[] for _ in range(k + 1)]
        row_deg = [0] * (k + 1)
        col_deg = [0] * (k + 1)

        for a, b in rowConditions:
            row_adj[a].append(b)
            row_deg[b] += 1
        for l, r in colConditions:
            col_adj[l].append(r)
            col_deg[r] += 1

        def topo_sort(in_deg, adj):
            q = deque([i for i in range(1, k + 1) if in_deg[i] == 0])
            idx = 0
            indices = [-1] * (k + 1)
            assigned = 0

            while q:
                num = q.popleft()
                indices[num] = idx
                idx += 1
                assigned += 1
    
                for nbr in adj[num]:
                    in_deg[nbr] -= 1
                    if in_deg[nbr] == 0:
                        q.append(nbr)

            if assigned != k:
                return []
            return indices

        if not (row_indices := topo_sort(row_deg, row_adj)):
            return []
        if not (col_indices := topo_sort(col_deg, col_adj)):
            return []

        mat = [[0] * k for _ in range(k)]
        for num, (r, c) in enumerate(zip(row_indices, col_indices)):
            if num > 0:
                mat[r][c] = num

        return mat