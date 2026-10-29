from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = defaultdict(list)

        for src, dst in tickets:
            adj[src].append(dst)

        res = ["JFK"]

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj or not adj[src]:
                return False

            temp = adj[src].copy()
            for i, dst in enumerate(temp):
                adj[src].pop(i)
                res.append(dst)
                if dfs(dst):
                    return True
                
                res.pop()
                adj[src].insert(i, dst)
            
            return False

        dfs("JFK")

        return res
        