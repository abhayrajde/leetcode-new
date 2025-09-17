import heapq
from collections import defaultdict

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foodToCuisine = {}
        self.foodToRating = {}
        self.cuisineHeap = defaultdict(list)

        for f, c, r in zip(foods, cuisines, ratings):
            self.foodToCuisine[f] = c
            self.foodToRating[f] = r
            heapq.heappush(self.cuisineHeap[c], (-r, f))  # max-heap by (-rating, lexicographically)

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.foodToCuisine[food]
        self.foodToRating[food] = newRating
        heapq.heappush(self.cuisineHeap[cuisine], (-newRating, food))  # push new value

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisineHeap[cuisine]
        # Lazy delete: pop until top is consistent with current rating
        while heap:
            rating, food = heap[0]
            if -rating == self.foodToRating[food]:
                return food
            heapq.heappop(heap)  # discard outdated entry

