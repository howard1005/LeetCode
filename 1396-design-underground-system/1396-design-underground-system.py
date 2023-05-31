from collections import defaultdict
class UndergroundSystem:

    def __init__(self):
        self.tots = defaultdict(lambda : (0,0))
        self.d = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.d[id] = (stationName,t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        ps,pt = self.d[id]
        tot,cnt = self.tots[(ps,stationName)]
        self.tots[(ps,stationName)] = (tot+(t-pt),cnt+1)
        
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        tot,cnt = self.tots[(startStation,endStation)]
        return tot/cnt


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)