class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x = y = z = False

        for t in triplets:
            if (
                t[0] > target[0]
                or t[1] > target[1]
                or t[2] > target[2]
            ):
                continue

            x |= t[0] == target[0]
            y |= t[1] == target[1]
            z |= t[2] == target[2]

            if x and y and z:
                return True

        return False
        