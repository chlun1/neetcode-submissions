class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = sum(1 for c in s if c == "1")
        return "1" * (ones - 1) + "0" * (len(s) - ones) + "1"
