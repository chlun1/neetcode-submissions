class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0

        def backtrack(start, current_subset):
            nonlocal total

            subtotal = 0
            for elem in current_subset:
                subtotal ^= elem

            total += subtotal
            
            for i in range(start, len(nums)):
                current_subset.append(nums[i])
                backtrack(i + 1, current_subset)
                current_subset.pop()

        backtrack(0, [])

        return total
