class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num

        res = []

        while nums:
            k = 0
            for i in range(maximumBit):
                if xor & (1 << i) == 0:
                    k = k | (1 << i)
    
            res.append(k)
            xor ^= nums.pop()
    
        return res
