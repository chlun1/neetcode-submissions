class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        def backtrack(r, c, char_idx):
            if (
                r < 0 or r >= rows or c < 0 or c >= cols
                or board[r][c] != word[char_idx]
            ):
                return False

            if char_idx == len(word) - 1:
                return True

            tmp = board[r][c]
            board[r][c] = ""

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if backtrack(nr, nc, char_idx + 1):
                    return True

            board[r][c] = tmp

            return False

        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True

        return False
        