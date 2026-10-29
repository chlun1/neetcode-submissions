class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        carry = 0

        for i in range(len(digits) - 1, -1, -1):
            digit = digits[i] + carry
            if i == len(digits) - 1:
                digit += 1
                
            carry = digit // 10
            res.append(digit % 10)

        if carry > 0:
            res.append(carry)

        return res[::-1]
        