class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target <= row[-1]:
                l, r = 0, len(row) - 1
                
                while l <= r:
                    mid = l + (r - l) // 2
                    guess = row[mid]

                    if guess == target:
                        return True
                    if guess > target:
                        r = mid - 1
                    else:
                        l = mid + 1

        return False
        