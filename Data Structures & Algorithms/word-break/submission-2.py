class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}

        def helper(i):
            if i == len(s):
                return True

            if i in cache:
                return cache[i]

            res = False

            for word in wordDict:
                if s[i: i + len(word)] == word:
                    if helper(i + len(word)):
                        res = True
                        break

            cache[i] = res
            return res

        return helper(0)
