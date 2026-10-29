class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char2idx = {c: i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            for j in range(len(word1)):
                if j == len(word2):
                    return False

                if (c1 := word1[j]) != (c2 := word2[j]):
                    if char2idx[c1] > char2idx[c2]:
                        return False
                    break

        return True
