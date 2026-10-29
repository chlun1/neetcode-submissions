class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        if len(nums) % 2:
            return False

        seen = set()
        for num in nums:
            if num in seen:
                seen.remove(num)
            else:
                seen.add(num)

        return len(seen) == 0
            