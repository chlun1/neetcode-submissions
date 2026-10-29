class Solution:
    def search_one_pass(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            guess = nums[mid]

            if guess == target:
                return mid

            if nums[l] <= guess:
                if guess < target:
                    l = mid + 1
                elif nums[l] > target:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if guess > target:
                    r = mid - 1
                elif nums[r] < target:
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

        l, r = 0, n - 1
        if target >= nums[pivot] and target <= nums[r]:
            l = pivot
        else:
            r = pivot - 1

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
        