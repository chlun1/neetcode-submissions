class CountSquares:
    def __init__(self):
        self.points = set()
        self.counts = {}

    def add(self, point: List[int]) -> None:
        point = tuple(point)
        self.points.add(point)
        self.counts[point] = self.counts.get(point, 0) + 1

    def count(self, point: List[int]) -> int:
        px, py = point[0], point[1]
        res = 0

        for x, y in self.points:
            if (
                abs(px - x) == abs(py - y)
                and px != x and py != y
                and (px, y) in self.points and (x, py) in self.points
            ):
                res += (
                    self.counts[(px, y)]
                    * self.counts[(x, py)]
                    * self.counts[(x, y)]
                )

        return res
