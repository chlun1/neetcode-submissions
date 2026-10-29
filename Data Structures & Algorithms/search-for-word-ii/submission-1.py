class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_idx = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        res = []
        root = TrieNode()

        for i, word in enumerate(words):
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.word_idx = i

        def backtrack(r, c, curr):
            if (
                r < 0 or c < 0 or r >= rows or c >= cols
                or board[r][c] not in curr.children
            ):
                return

            char = board[r][c]
            curr = curr.children[char]

            if curr.word_idx is not None:
                res.append(words[curr.word_idx])
                curr.word_idx = None

            board[r][c] = ""

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                backtrack(r + dr, c + dc, curr)

            board[r][c] = char

        for r in range(rows):
            for c in range(cols):
                backtrack(r, c, root)

        return res
