class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0

        def backtrack(start, subtotal):
            nonlocal total
            total += subtotal
            
            for i in range(start, len(nums)):
                backtrack(i + 1, subtotal ^ nums[i])

        backtrack(0, 0)

        return total
