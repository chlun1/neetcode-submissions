from collections import defaultdict, deque


class Solution:
    def is_neighbour(self, s1, s2):
        n_diff = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                n_diff += 1
                if n_diff > 1:
                    return False

        return True

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 1

        wordList.append(beginWord)
        adj = defaultdict(list)

        for i in range(len(wordList)):
            s1 = wordList[i]
            for j in range(i + 1, len(wordList)):
                s2 = wordList[j]
                if self.is_neighbour(s1, s2):
                    adj[s1].append(s2)
                    adj[s2].append(s1)

        if endWord not in adj:
            return 0

        q = deque([beginWord])
        visited = set()
        res = 1

        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                for nbr in adj[curr]:
                    if nbr == endWord:
                        return res + 1
                    if nbr not in visited:
                        q.append(nbr)
                        visited.add(nbr)

            res += 1

        return 0
