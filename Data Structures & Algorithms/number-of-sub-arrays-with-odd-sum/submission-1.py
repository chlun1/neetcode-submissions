class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        res = 0
        curr_sum = 0
        even_count = 1
        odd_count = 0
        MOD = 10**9 + 7

        for num in arr:
            curr_sum += num
            if curr_sum % 2:
                res = (res + even_count) % MOD
                odd_count += 1
            else:
                res = (res + odd_count) % MOD
                even_count += 1

        return res
