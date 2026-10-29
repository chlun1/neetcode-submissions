class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counts1 = [0] * 26
        counts2 = [0] * 26
        for c in s1:
            counts1[ord(c) - ord("a")] += 1

        target = set([tuple(counts1)])

        l = 0
        for r in range(len(s2)):
            if r - l + 1 > len(s1):
                counts2[ord(s2[l]) - ord("a")] -= 1
                l += 1

            c = s2[r]
            counts2[ord(c) - ord("a")] += 1
            if tuple(counts2) in target:
                return True

        return False
        