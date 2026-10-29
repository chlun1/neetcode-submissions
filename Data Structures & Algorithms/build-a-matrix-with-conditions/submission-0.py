from collections import defaultdict, deque


class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        row_adj = defaultdict(list)
        col_adj = defaultdict(list)
        row_deg = [0] * (k + 1)
        col_deg = [0] * (k + 1)
        row_nums = set()
        col_nums = set()

        for a, b in rowConditions:
            row_adj[a].append(b)
            row_deg[b] += 1
            row_nums.add(a)
            row_nums.add(b)
        for l, r in colConditions:
            col_adj[l].append(r)
            col_deg[r] += 1
            col_nums.add(l)
            col_nums.add(r)

        q = deque([i for i in row_nums if row_deg[i] == 0])
        indices = [[-1, -1] for _ in range(k + 1)]
        assigned = 0
        row_idx = 0

        while q:
            num = q.popleft()
            indices[num][0] = row_idx
            row_idx += 1
            assigned += 1

            for nbr in row_adj[num]:
                row_deg[nbr] -= 1
                if row_deg[nbr] == 0:
                    q.append(nbr)

        if assigned != len(row_nums):
            return []

        q = deque([i for i in col_nums if col_deg[i] == 0])
        assigned = 0
        col_idx = 0

        while q:
            num = q.popleft()
            indices[num][1] = col_idx
            col_idx += 1
            assigned += 1

            for nbr in col_adj[num]:
                col_deg[nbr] -= 1
                if col_deg[nbr] == 0:
                    q.append(nbr)


        if assigned != len(col_nums):
            return []

        mat = [[0] * k for _ in range(k)]
        r0, c0 = 0, 0
        for num, row_col in enumerate(indices):
            if num == 0:
                continue
            r, c = row_col[0], row_col[1]
            if r == -1:
                r = r0
                r0 += 1
            if c == -1:
                c = c0
                c0 += 1
            mat[r][c] = num

        return mat