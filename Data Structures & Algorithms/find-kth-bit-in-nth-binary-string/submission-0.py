class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        res = "0"
        
        for _ in range(n):
            tmp = "".join("0" if x == "1" else "1" for x in res[::-1])
            res = res + "1" + tmp

        return res[k - 1]
