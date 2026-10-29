class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        root = TrieNode()

        for word in dictionary:
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.is_end = True

        n = len(s)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            res = 1 + dp[i + 1]
            curr = root
            for j in range(i, n):
                if s[j] not in curr.children:
                    break

                curr = curr.children[s[j]]
                if curr.is_end:
                    res = min(res, dp[j + 1])

            dp[i] = res

        return dp[0]
