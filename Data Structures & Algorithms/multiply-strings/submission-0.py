class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def str_to_num(s):
            str2int = {
                "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, 
                "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
            }

            num = 0
            exp = 1
            for i in range(len(s) - 1, -1, -1):
                num += str2int[s[i]] * exp
                exp *= 10

            return num

        return str(str_to_num(num1) * str_to_num(num2))
