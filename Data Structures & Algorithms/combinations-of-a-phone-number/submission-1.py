class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = []

        digit_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, curr):
            if i == len(digits):
                res.append("".join(curr))
                return

            for c in digit_map[digits[i]]:
                curr.append(c)
                backtrack(i + 1, curr)
                curr.pop()

        backtrack(0, [])

        return res
        