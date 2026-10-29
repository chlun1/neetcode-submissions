class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_idx = None


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        root = TrieNode()

        for i, word in enumerate(wordDict):
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.word_idx = i

        res = []

        def backtrack(i, words):
            if i == len(s):
                res.append(" ".join(words))
                return

            curr = root
            for j in range(i, len(s)):
                c = s[j]
                if c not in curr.children:
                    break

                curr = curr.children[c]
                if curr.word_idx is not None:
                    words.append(wordDict[curr.word_idx])
                    backtrack(j + 1, words)
                    words.pop()

        backtrack(0, [])

        return res
