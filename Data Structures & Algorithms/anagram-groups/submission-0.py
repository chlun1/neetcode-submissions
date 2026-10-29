from collections import defaultdict


class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        counts = defaultdict(int)

        for i in range(len(s)):
            counts[s[i]] += 1
            counts[t[i]] -= 1

        for count in counts.values():
            if count != 0:
                return False

        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        processed = set()

        for i in range(len(strs)):
            if i in processed:
                continue
            
            s = strs[i]
            key = "".join(sorted(s))
            group[key].append(s)
            processed.add(i)

            for j in range(i + 1, len(strs)):
                if j in processed:
                    continue

                t = strs[j]
                if self.isAnagram(s, t):
                    group[key].append(t)
                    processed.add(j)

        return list(group.values())
        