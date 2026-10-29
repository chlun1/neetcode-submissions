from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        in_degrees = [0] * numCourses

        for dest, src in prerequisites:
            adj[src].append(dest)
            in_degrees[dest] += 1

        q = deque([
            dest for dest, deg in enumerate(in_degrees) if deg == 0
        ])

        res = []

        while q:
            course = q.popleft()
            res.append(course)
            for dest in adj[course]:
                in_degrees[dest] -= 1
                if in_degrees[dest] == 0:
                    q.append(dest)

        return res if len(res) == numCourses else []
