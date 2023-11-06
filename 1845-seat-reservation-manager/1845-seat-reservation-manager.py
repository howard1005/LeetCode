from heapq import heappush,heappop

class SeatManager:

    def __init__(self, n: int):
        self.hq = [_ for _ in range(1,n+1)]
        

    def reserve(self) -> int:
        return heappop(self.hq)
        

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.hq,seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)