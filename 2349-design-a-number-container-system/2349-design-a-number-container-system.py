from heapq import heappush,heappop

class NumberContainers:

    def __init__(self):
        self.d = defaultdict(int)
        self.rd = defaultdict(list)
        
    def change(self, index: int, number: int) -> None:            
        self.d[index] = number
        hq = self.rd[number]
        heappush(hq,index)
        
    def find(self, number: int) -> int:
        hq = self.rd[number]
        while hq and self.d[hq[0]] != number:
            heappop(hq)
        return hq[0] if hq else -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)