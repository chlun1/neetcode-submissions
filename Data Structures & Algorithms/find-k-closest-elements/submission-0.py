class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr) - 1

        while True:
            if r - l + 1 == k:
                return arr[l:r + 1]

            if abs(arr[l] - x) < abs(arr[r] - x):
                r -= 1
            elif abs(arr[l] - x) > abs(arr[r] - x):
                l += 1
            else:
                if arr[l] < arr[r]:
                    r -= 1
                else:
                    l += 1
