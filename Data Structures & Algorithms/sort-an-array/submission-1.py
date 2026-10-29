import random


class Solution:
    def partition(self, nums: List[int], low: int, high: int) -> int:
        # Pick a random index and swap with high to avoid worst-case O(n^2)
        rand_idx = random.randint(low, high)
        nums[rand_idx], nums[high] = nums[high], nums[rand_idx]

        pivot = nums[high]
        i = low - 1

        for j in range(low, high):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return i + 1

    def _sort(self, nums: List[int], low: int, high: int):
        if low < high:
            pivot_index = self.partition(nums, low, high)
            self._sort(nums, low, pivot_index - 1)
            self._sort(nums, pivot_index + 1, high)

    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums

        self._sort(nums, 0, len(nums) - 1)
        return nums
        