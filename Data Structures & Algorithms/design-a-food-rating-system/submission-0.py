import heapq
from collections import defaultdict


class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisines = defaultdict(list)
        self.foods = {}

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.cuisines[cuisine].append((-rating, food))
            self.foods[food] = (cuisine, -rating)

        [heapq.heapify(x) for x in self.cuisines.values()]

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, _ = self.foods[food]
        ratings = self.cuisines[cuisine]
        heapq.heappush(ratings, (-newRating, food))
        self.foods[food] = (cuisine, -newRating)

    def highestRated(self, cuisine: str) -> str:
        ratings = self.cuisines[cuisine]

        while True:
            rating, food = ratings[0]
            _, actual_rating = self.foods[food]
    
            if actual_rating == rating:
                return food

            heapq.heappop(ratings)
