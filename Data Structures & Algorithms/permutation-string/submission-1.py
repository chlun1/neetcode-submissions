class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counts1 = [0] * 26
        counts2 = [0] * 26
        for c in s1:
            counts1[ord(c) - ord("a")] += 1

        matches = sum(
            1 if counts1[i] == counts2[i] else 0
            for i in range(26)
        )
        l = 0

        for r in range(len(s2)):
            if r - l + 1 > len(s1):
                index = ord(s2[l]) - ord("a")
                counts2[index] -= 1
                if counts1[index] == counts2[index]:
                    matches += 1
                elif counts1[index] - 1 == counts2[index]:
                    matches -= 1
                l += 1

            index = ord(s2[r]) - ord("a")
            counts2[index] += 1
            if counts1[index] == counts2[index]:
                matches += 1
            elif counts1[index] + 1 == counts2[index]:
                matches -= 1

            if matches == 26:
                return True

        return matches == 26
        