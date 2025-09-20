from bisect import bisect_left,bisect_right

class Router:

    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.dq = deque()
        self.sd = set()
        self.d = defaultdict(deque)


    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        t = (source,destination,timestamp)
        if t in self.sd:
            return False
        if len(self.dq) == self.memoryLimit:
            delt = self.dq.popleft()
            self.sd.remove(delt)
            self.d[delt[1]].popleft()
        self.dq.append(t)
        self.sd.add(t)
        self.d[destination].append(t)
        return True


    def forwardPacket(self) -> List[int]:
        if not self.dq:
            return []
        ft = self.dq.popleft()
        self.sd.remove(ft)
        self.d[ft[1]].popleft()
        return ft
        

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        ret = 0
        
        l = self.d[destination]
        i = bisect_left(l,startTime,key=lambda x:x[2])
        j = bisect_right(l,endTime,key=lambda x:x[2])
        ret = j-i

        return ret


        




# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)