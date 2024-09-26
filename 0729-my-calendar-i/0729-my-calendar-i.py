class MyCalendar:

    def __init__(self):
        self.tick = [(-1,0),(1000000001,1000000002)]

    def book(self, start: int, end: int) -> bool:
        idx = -1
        for i in range(len(self.tick)-1):
            if  self.tick[i][1] <= start and end <= self.tick[i+1][0]:
                idx = i+1
        if idx != -1:
            self.tick.insert(idx,(start,end))
            return True
        else:
            return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)