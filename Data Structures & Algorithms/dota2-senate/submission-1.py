class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        removed = set()
        skip_radiants = 0
        skip_dires = 0
        radiants = 0
        dires = 0
    
        for c in senate:
            if c == "R":
                radiants += 1
            else:
                dires += 1
    
        while True:
            for i, c in enumerate(senate):
                if i in removed:
                    continue
    
                if dires == 0:
                    return "Radiant"
                if radiants == 0:
                    return "Dire"	
                
                if skip_radiants > 0 and c == "R":
                    removed.add(i)
                    radiants -= 1
                    skip_radiants -= 1
                    continue
    
                if skip_dires > 0 and c == "D":
                    removed.add(i)
                    dires -= 1
                    skip_dires -= 1
                    continue
    
                if c == "R":
                    skip_dires += 1
                else:
                    skip_radiants += 1
            