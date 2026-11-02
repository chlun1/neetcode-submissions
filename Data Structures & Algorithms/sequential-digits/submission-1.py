class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        inc = {
            1: 1, 2: 11, 3: 111, 4: 1111, 5: 11111, 6: 111111, 7: 1111111,
            8: 11111111, 9: 111111111, 10: 1111111111, 11: 11111111111,
        }

        def extract_digits(num):
            digits = []
            while num:
                d = num % 10
                digits.append(d)
                num //= 10

            return digits[::-1]

        digits = extract_digits(low)
        start = digits[0]
        n_digits = len(digits)
        res = []
        x = -1

        while x <= high:
            if start + n_digits > 10:
                start = 1
                n_digits += 1
                x = -1

            if x == -1:
                d = start
                x = d
        
                for _ in range(n_digits - 1):
                    x *= 10
                    d += 1
                    x += d
    
            if low <= x <= high:
                res.append(x)

            x += inc[n_digits]

            start += 1

        return res
        