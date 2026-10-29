class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        for i in range(n):
            curr_gas = gas[i] - cost[i]
            j = (i + 1) % n

            while curr_gas >= 0 and j != i:
                curr_gas += gas[j] - cost[j]
                j = (j + 1) % n

            if j == i and curr_gas >= 0:
                return i

        return -1
        