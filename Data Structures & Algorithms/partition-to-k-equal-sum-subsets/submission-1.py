class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums.sort(reverse=True)
        total = sum(nums)
        if total % k != 0:
            return False
        target = sum(nums) // k

        def backtrack(i, subset_sums):
            if i == len(nums):
                return all(s == target for s in subset_sums)

            num = nums[i]

            for j in range(k):
                if j > 0 and subset_sums[j - 1] == subset_sums[j]:
                    continue

                subset_sums[j] += num
                if subset_sums[j] <= target and backtrack(i + 1, subset_sums):
                    return True
                subset_sums[j] -= num

                if subset_sums[j] == 0:
                    break
                
            return False

        return backtrack(0, [0] * k)
        