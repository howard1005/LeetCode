class MyCalendarTwo:

    def __init__(self):
        self.l = []

    def book(self, start: int, end: int) -> bool:
        # print(self.l, start, end)
            
        tl = []

        def intersection(r1,r2):
            return (max(r1[0],r2[0]),min(r1[1],r2[1]))

        a,b = start,end-1
        for i,(c,d,t) in enumerate(self.l):
            if b<c:
                tl.append((a,b,0))
                tl.extend(self.l[i:])
                b = -1
                break

            it = intersection((a,b),(c,d))
            if it[0]<=it[1]:
                if t == 1:
                    return False
            else:
                tl.append((c,d,t))
                continue

            if a<it[0]:
                tl.append((a,it[0]-1,0))
            if c<it[0]:
                tl.append((c,it[0]-1,0))
            tl.append((it[0],it[1],1))
            a = it[1]+1
            if it[1]<b:
                 pass
            if it[1]<d:
                 tl.append((it[1]+1,d,0))

        if a<=b:
            tl.append((a,b,0))
            
        self.l = tl

        # print(self.l, start, end)
        
        return True

            
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)