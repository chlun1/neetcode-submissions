class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num

        res = []

        for i in range(len(nums) - 1, -1, -1):
            k = (1 << maximumBit) - 1
            res.append(k ^ xor)
            xor ^= nums[i]
    
        return res
