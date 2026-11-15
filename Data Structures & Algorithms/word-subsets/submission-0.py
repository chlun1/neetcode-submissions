from collections import Counter


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        counts = {}

        for word in words2:
            tmp = Counter(word)

            if not counts:
                counts = tmp
            else:
                for c, count in tmp.items():
                    if c not in counts or counts[c] < count:
                        counts[c] = count

        res = []

        for word in words1:
            counts1 = Counter(word)
            
            satisfy = True
            for c, count in counts.items():
                if c not in counts1 or counts1[c] < count:
                    satisfy = False
                    break

            if satisfy:
                res.append(word)

        return res
