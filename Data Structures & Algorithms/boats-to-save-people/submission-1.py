class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # [1,2,4,5]
        # [1,2,2,3,3]
        people.sort()
        n = len(people)
        res = 0
        l, r = 0, n - 1

        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
            else:
                r -= 1

            res += 1

        return res
