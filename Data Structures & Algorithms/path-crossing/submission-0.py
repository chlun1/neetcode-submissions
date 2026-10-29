class Solution:
    def isPathCrossing(self, path: str) -> bool:
        r, c = 0, 0
        visited = {(r, c)}

        for p in path:
            if p == "N":
                r -= 1
            elif p == "S":
                r += 1
            elif p == "E":
                c += 1
            else:
                c -= 1

            if (r, c) in visited:
                return True
            
            visited.add((r, c))

        return False
        