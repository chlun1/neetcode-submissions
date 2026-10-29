from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        in_degrees = [0] * numCourses

        for dest, src in prerequisites:
            adj[src].append(dest)
            in_degrees[dest] += 1

        q = deque([
            dest for dest, in_deg in enumerate(in_degrees)
            if in_deg == 0
        ])

        n_courses = 0
        while q:
            course = q.popleft()
            n_courses += 1

            for dest in adj[course]:
                in_degrees[dest] -= 1
                if in_degrees[dest] == 0:
                    q.append(dest)

        return n_courses == numCourses
        