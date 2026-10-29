from collections import defaultdict, deque


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        in_degrees = [0] * numCourses

        for src, dest in prerequisites:
            adj[src].append(dest)
            in_degrees[dest] += 1

        q = deque()
        ancestors = defaultdict(set)
        for course in range(numCourses):
            if in_degrees[course] == 0:
                q.append(course)
                ancestors[course] = set([course])

        while q:
            for _ in range(len(q)):
                course = q.popleft()

                for dest in adj[course]:
                    in_degrees[dest] -= 1
                    ancestors[dest] |= ancestors[course]
                    if in_degrees[dest] == 0:
                        ancestors[dest].add(dest)
                        q.append(dest)

        return [
            u in ancestors[v]
            for u, v in queries
        ]
