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

        if endWord not in wordList:
            return 0

        wordList.append(beginWord)
        adj = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                adj[pattern].append(word)

        q = deque([beginWord])
        visited = {beginWord}
        res = 1

        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                for i in range(len(curr)):
                    pattern = curr[:i] + "*" + curr[i + 1:]
                    for nbr in adj[pattern]:
                        if nbr == endWord:
                            return res + 1
                        if nbr not in visited:
                            q.append(nbr)
                            visited.add(nbr)
    
            res += 1

        return 0
