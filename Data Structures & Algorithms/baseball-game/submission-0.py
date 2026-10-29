class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        total = 0

        for op in operations:
            if op == "+":
                s = record[-1] + record[-2]
                total += s
                record.append(s)
            elif op == "C":
                total -= record.pop()
            elif op == "D":
                s = 2 * record[-1]
                total += s
                record.append(s)
            else:
                s = int(op)
                total += s
                record.append(s)

        return total
        