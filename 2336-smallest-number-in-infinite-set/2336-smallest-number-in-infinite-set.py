from heapq import heappush, heappop

class SmallestInfiniteSet:

    def __init__(self):
        self.d = {}
        self.mx = 1
        self.hq = []
        

    def popSmallest(self) -> int:
        if self.hq and self.mx > self.hq[0]:
            ret = heappop(self.hq)
            del self.d[ret]
            return ret
        ret = self.mx
        self.mx += 1
        return ret
        

    def addBack(self, num: int) -> None:
        if self.mx > num and num not in self.d:
            self.d[num] = 1
            heappush(self.hq, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)