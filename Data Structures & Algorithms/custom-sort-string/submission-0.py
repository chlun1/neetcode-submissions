class Solution:
    def customSortString(self, order: str, s: str) -> str:
        indices = {c: i for i, c in enumerate(order)}

        return "".join(sorted(s, key=lambda c: indices.get(c, len(s))))
        