class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res = 1
        curr_len = 1
        prev = arr[0]
        inc = None

        for i in range(1, len(arr)):
            num = arr[i]
            curr_len_old = curr_len
            inc_old = inc

            if curr_len == 1:
                if prev < num:
                    inc = False
                    curr_len += 1
                elif prev > num:
                    inc = True
                    curr_len += 1
            else:
                if inc and num < prev:
                    curr_len = 2
                elif not inc and num > prev:
                    curr_len = 2
                elif prev == num:
                    curr_len = 1
                else:
                    curr_len += 1
                    inc = not inc

            prev = num
            res = max(res, curr_len)

            #print(f"{i}: {curr_len_old} -> {curr_len}, {inc_old} -> {inc}")

        return res
        