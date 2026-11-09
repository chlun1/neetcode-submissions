class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        invert = False
        length = 2 ** n - 1
        
        while length > 1:
            half = length // 2

            if k <= half:
                length = half
            elif k > half + 1:
                k = length - k + 1
                length = half
                invert = not invert
            else:
                return "1" if not invert else "0"

        return "0" if not invert else "1"
