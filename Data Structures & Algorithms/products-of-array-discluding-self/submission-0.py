class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prods = []
        prod = 1
        for num in nums:
            prod *= num
            prods.append(prod)

        prods_rev = []
        prod = 1
        for num in reversed(nums):
            prod *= num
            prods_rev.append(prod)
        prods_rev.reverse()

        res = []
        for i in range(len(nums)):
            prod = 1
            if i > 0:
                prod *= prods[i - 1]
            if i < len(nums) - 1:
                prod *= prods_rev[i + 1]
            res.append(prod)

        return res
