class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        notes = {5: 0, 10: 0, 20: 0}

        for bill in bills:
            if bill != 5:
                change_needed = bill - 5
                for note in [20, 10, 5]:
                    while notes[note] > 0 and note <= change_needed:
                        change_needed -= note
                        notes[note] -= 1
                    
                if change_needed > 0:
                    return False

            notes[bill] += 1

        return True
        