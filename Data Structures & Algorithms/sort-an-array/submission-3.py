class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.sort(nums)

    def sort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        left_sorted = self.sort(left)
        right_sorted = self.sort(right)

        return self.merge(left_sorted, right_sorted)

    def merge(self, left, right):
        n = len(left)
        m = len(right)
        res = [0] * (n + m)
        i, j, k = 0, 0, 0

        while i < n and j < m:
            if left[i] <= right[j]:
                res[k] = left[i]
                i += 1
            else:
                res[k] = right[j]
                j += 1

            k += 1

        while i < n:
            res[k] = left[i]
            i += 1
            k += 1

        while j < m:
            res[k] = right[j]
            j += 1
            k += 1

        return res
