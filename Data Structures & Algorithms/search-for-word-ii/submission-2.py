class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_idx = None
        self.ref = 0


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        res = []
        root = TrieNode()

        for i, word in enumerate(words):
            curr = root
            curr.ref += 1
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
                curr.ref += 1
            curr.word_idx = i

        def backtrack(r, c, curr):
            if (
                r < 0 or c < 0 or r >= rows or c >= cols
                or board[r][c] not in curr.children
            ):
                return 0

            char = board[r][c]
            parent = curr
            curr = curr.children[char]
            found = 0

            if curr.word_idx is not None:
                res.append(words[curr.word_idx])
                curr.word_idx = None
                found += 1

            board[r][c] = ""

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                found += backtrack(r + dr, c + dc, curr)

            board[r][c] = char
            curr.ref -= found
            if curr.ref == 0:
                del parent.children[char]

            return found

        for r in range(rows):
            for c in range(cols):
                backtrack(r, c, root)

        return res
