class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: [] for word in words for c in word}

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            min_len = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                # Order is invalid
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].append(w2[j])
                    break

        print(adj)

        visited = {}
        res = []

        def dfs(c):
            if c in visited:
                # Loop encountered if visited[c] is True
                return visited[c]
                                
            visited[c] = True

            for nei in adj[c]:
                if dfs(nei):
                    return True

            visited[c] = False
            res.append(c)

        for c in adj.keys():
            if dfs(c):
                return ""

        return "".join(res[i] for i in range(len(res) - 1, -1, -1))
