class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        root = TrieNode()

        for word in dictionary:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.is_end = True

        cache = {}

        def helper(i):
            if i in cache:
                return cache[i]

            if i == len(s):
                return 0

            res = 1 + helper(i + 1)
            curr = root
            
            for j in range(i, len(s)):
                if s[j] not in curr.children:
                    break

                curr = curr.children[s[j]]
                if curr.is_end:
                    res = min(res, helper(j + 1))

            cache[i] = res

            return res

        return helper(0)
