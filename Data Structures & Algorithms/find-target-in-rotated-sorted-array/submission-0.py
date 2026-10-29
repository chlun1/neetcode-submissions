class Solution:
    def binary_search(self, nums, target):
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            guess = nums[mid]
            if guess == target:
                return mid
            if guess > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1

    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        pivot = 0

        while l <= r:
            mid = l + (r - l) // 2
            if mid < n - 1 and nums[mid] > nums[mid + 1]:
                pivot = mid + 1
                break
            elif mid > 0 and nums[mid] < nums[mid - 1]:
                pivot = mid
                break
            elif nums[l] < nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        res = self.binary_search(nums[:pivot], target)
        if res != -1:
            return res
        res = self.binary_search(nums[pivot:], target)
        if res != -1:
            return pivot + res

        return -1
        