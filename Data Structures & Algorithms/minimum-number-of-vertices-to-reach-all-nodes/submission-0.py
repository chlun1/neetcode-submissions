from collections import defaultdict


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        in_degrees = defaultdict(int)

        for _, v in edges:
            in_degrees[v] += 1

        return [x for x in range(n) if in_degrees[x] == 0]
        