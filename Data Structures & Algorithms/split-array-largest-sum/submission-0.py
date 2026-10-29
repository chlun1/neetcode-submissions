class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def helper(target):
            total = 0
            n_subarrays = 1

            for num in nums:
                total += num
                if total > target:
                    n_subarrays += 1
                    total = num

            return n_subarrays <= k

        l = max(nums)
        r = sum(nums)
        res = r

        while l <= r:
            mid = l + (r - l) // 2

            if helper(mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1

        return res
        