class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = []
        negatives = []
        res = []

        for num in nums:
            if num > 0:
                positives.append(num)
            else:
                negatives.append(num)

        for pos, neg in zip(positives, negatives):
            res.append(pos)
            res.append(neg)

        return res
