class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}

        def dfs(i, j):
            if i == len(word1) and j == len(word2):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]

            if i == len(word1) and j < len(word2):
                # word1 too short. Need to insert
                res = 1 + dfs(i, j + 1)
            elif i < len(word1) and j == len(word2):
                # word1 too long. Need to delete
                res = 1 + dfs(i + 1, j)
            elif word1[i] == word2[j]:
                res = dfs(i + 1, j + 1)
            else:
                res = 1 + min(
                    dfs(i + 1, j + 1), # Replace
                    dfs(i, j + 1), # Insert
                    dfs(i + 1, j), # Delete
                )

            cache[(i, j)] = res
    
            return res

        return dfs(0, 0)
        