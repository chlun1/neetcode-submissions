class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])
        seen_cols = [set() for _ in range(cols)]
        
        for i in range(rows):
            seen_rows = set()
            if i % 3 == 0:
                seen_sqrs = [set() for _ in range(3)]

            for j in range(cols):
                num = board[i][j]
                if num == ".":
                    continue
                if (
                    num in seen_rows
                    or num in seen_cols[j]
                    or num in seen_sqrs[j // 3]
                ):
                    return False

                seen_rows.add(num)
                seen_cols[j].add(num)
                seen_sqrs[j // 3].add(num)

        return True
        