class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        total = 0
        for i in range(len(customers)):
            total += customers[i] * (1 - grumpy[i])

        window = 0
        l = 0
        res = total

        for r in range(len(customers)):
            window += customers[r] * grumpy[r]

            if r - l + 1 > minutes:
                window -= customers[l] * grumpy[l]
                l += 1

            res = max(res, total + window)

        return res
