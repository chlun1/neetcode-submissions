class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = [0] * 26
        for c in magazine:
            counts[ord(c) - ord("a")] += 1

        for c in ransomNote:
            idx = ord(c) - ord("a")
            counts[idx] -= 1
            if counts[idx] < 0:
                return False

        return True
        