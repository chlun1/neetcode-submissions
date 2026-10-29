from collections import defaultdict, deque


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(set)
        in_degrees = defaultdict(int)
        chars = set()
        for word in words:
            chars.update(word)
        
        for i in range(1, len(words)):
            w1 = words[i - 1]
            w2 = words[i]
            is_prefix = True
            for j in range(min(len(w1), len(w2))):
                c1, c2 = w1[j], w2[j]
                if c1 != c2:
                    if c2 not in adj[c1]:
                        adj[c1].add(c2)
                        in_degrees[c2] += 1
                    is_prefix = False
                    break

            if is_prefix and len(w1) > len(w2):
                return ""

        q = deque([c for c in chars if in_degrees[c] == 0])
        res = []

        while q:
            char = q.popleft()
            res.append(char)

            for next_char in adj[char]:
                in_degrees[next_char] -= 1
                if in_degrees[next_char] == 0:
                    q.append(next_char)

        return "".join(res) if len(res) == len(chars) else ""
        