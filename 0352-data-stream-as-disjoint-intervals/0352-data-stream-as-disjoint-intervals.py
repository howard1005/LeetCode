from sortedcontainers import SortedList

class SummaryRanges:

    def __init__(self):
        self.l = SortedList()
        self.d = {}
        
    def addNum(self, value: int) -> None:
        if value in self.d:
            return
        self.d[value] = 1
        r = [value,value]
        i = self.l.bisect_left(r)
        isL,isR = False,False
        if i>0 and self.l[i-1][1] == r[0]-1:
            self.l[i-1][1] = r[0]
            isL = True
        if i<len(self.l) and self.l[i][0] == r[1]+1:
            self.l[i][0] = r[1]
            isR = True
        if isL and isR:
            self.l[i-1][1] = self.l[i][1]
            del self.l[i]
        if not isL and not isR:
            self.l.add(r)

    def getIntervals(self) -> List[List[int]]:
        return self.l


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()