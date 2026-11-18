class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        if len(s) == 1:
            return s

        bits = sorted(s, reverse=True)

        for i in range(len(bits) - 1):
            if bits[i + 1] == "0":
                bits[i], bits[-1] = bits[-1], bits[i]
                break

        return "".join(bits)
        