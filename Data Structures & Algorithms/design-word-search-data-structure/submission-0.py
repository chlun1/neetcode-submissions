class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_end = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]

        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root

        def _search(curr, char_idx):
            if char_idx == len(word):
                return curr.is_end

            char = word[char_idx]
            if char == ".":
                return any(
                    _search(node, char_idx + 1)
                    for node in curr.children.values()
                )
            if char not in curr.children:
                return False

            return _search(curr.children[char], char_idx + 1)

        return _search(self.root, 0)
