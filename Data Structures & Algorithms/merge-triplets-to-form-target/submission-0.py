class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        def valid(triplet):
            for i in range(3):
                if triplet[i] > target[i]:
                    return False

            return True

        def match_any(triplet):
            for i in range(3):
                if triplet[i] == target[i]:
                    return True

            return False

        curr = None

        for triplet in triplets:
            if not valid(triplet):
                continue

            if curr == target:
                return True

            if curr is None:
                curr = triplet
                continue

            if match_any(triplet):
                curr = [
                    max(curr[0], triplet[0]),
                    max(curr[1], triplet[1]),
                    max(curr[2], triplet[2]),
                ]

        return curr == target
        