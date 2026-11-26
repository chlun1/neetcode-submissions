from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def comparator(a, b):
            if a == b:
                return 0

            if a + b < b + a:
                return -1
            
            return 1

        res = "".join(
            sorted(
                map(str, nums),
                key=cmp_to_key(comparator),
                reverse=True),
        )

        return "0" if res[0] == "0" else res
        