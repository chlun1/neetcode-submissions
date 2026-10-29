class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        total = 0
        for num in nums:
            total ^= num

        res = []

        distinguishing_bit = total & (-total)
        a = b = 0
        for num in nums:
            if num & distinguishing_bit:
                a ^= num
            else:
                b ^= num

        return [a, b]
    