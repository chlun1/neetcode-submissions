class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char2idx = {c: i for i, c in enumerate(order)}

        prev = words[0]
        for i in range(1, len(words)):
            word = words[i]

            if len(prev) > len(word) and prev[:len(word)] == word:
                return False

            for c1, c2 in zip(prev, word):
                if c1 == c2:
                    continue
                else:
                    if char2idx[c1] > char2idx[c2]:
                        return False
                    break

            prev = word

        return True
