from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_count = Counter(ransomNote)
        m_count = Counter(magazine)

        for c, count in r_count.items():
            if c not in m_count or m_count[c] < count:
                return False

        return True
        