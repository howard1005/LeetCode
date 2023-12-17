from heapq import heappush,heappop

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.hqd = defaultdict(list)
        self.fd = {}
        for r,f,c in zip(ratings,foods,cuisines):
            self.fd[f] = (r,c)
            heappush(self.hqd[c],(-r,f))
            

    def changeRating(self, food: str, newRating: int) -> None:
        c = self.fd[food][1]
        heappush(self.hqd[c],(-newRating,food))
        self.fd[food] = (newRating,c)
        

    def highestRated(self, cuisine: str) -> str:
        hq = self.hqd[cuisine]
        while -hq[0][0] != self.fd[hq[0][1]][0]:
            heappop(hq)
        return hq[0][1]
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)