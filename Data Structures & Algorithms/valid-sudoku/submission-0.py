from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])
        col_nums = [defaultdict(int) for _ in range(cols)]

        for i in range(rows):
            row_nums = defaultdict(int)
            if i % 3 == 0:
                sqr_nums = [defaultdict(int) for _ in range(3)]

            for j in range(cols):
                num = board[i][j]
                if num == ".":
                    continue
                row_nums[num] += 1
                if row_nums[num] > 1:
                    return False
                col_nums[j][num] += 1
                if col_nums[j][num] > 1:
                    return False
                sqr_nums[j // 3][num] += 1
                if sqr_nums[j // 3][num] > 1:
                    return False

        return True
        