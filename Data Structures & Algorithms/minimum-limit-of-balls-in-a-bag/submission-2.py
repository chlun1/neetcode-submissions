class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        nums.sort()

        def condition(x):
            count = 0

            for i in range(len(nums) - 1, -1, -1):
                if nums[i] <= x:
                    break

                count += nums[i] // x
                if nums[i] % x == 0:
                    count -= 1

            return count <= maxOperations

        l = 1
        r = nums[-1]
        res = r

        while l <= r:
            mid = l + (r - l) // 2

            if condition(mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1

        return res
