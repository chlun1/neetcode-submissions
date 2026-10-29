class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        non_zeros = [i for i, box in enumerate(boxes) if box == "1"]
        res = []

        for i in range(len(boxes)):
            ans = 0
            for idx in non_zeros:
                ans += abs(idx - i)
            res.append(ans)

        return res
