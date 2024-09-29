class LN:
    def __init__(self,i=0,cnt=0,prev=None,next=None):
        self.i = i
        self.sd = set()
        self.prev = prev
        self.next = next

    def getKey(self):
        ret = self.sd.pop()
        self.sd.add(ret)
        return ret

    def add(self, key):
        self.sd.add(key)

    def remove(self, key):
        if key in self.sd:
            self.sd.remove(key)
        if self.i and not self.sd:
            self._del()

    def _del(self):
        self.prev.next = self.next
        self.next.prev = self.prev

    def getIncLN(self):
        if self.next.i == self.i+1:
            return self.next
        newLN = LN(self.i+1,0,self,self.next)
        self.next.prev = newLN
        self.next = newLN
        return newLN

    def getDecLN(self):
        if self.prev.i == self.i-1:
            return self.prev
        newLN = LN(self.i-1,0,self.prev,self)
        self.prev.next = newLN
        self.prev = newLN
        return newLN
        


class AllOne:

    def __init__(self):
        self.head = LN()
        self.tail = LN()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.d = defaultdict(lambda: (0,self.head))

    def inc(self, key: str) -> None:
        i,ln = self.d[key]
        nln = ln.getIncLN()
        nln.add(key)
        ln.remove(key)
        self.d[key] = (i+1,nln)
        
    def dec(self, key: str) -> None:
        i,ln = self.d[key]
        if i == 1:
            ln.remove(key)
            del self.d[key]
            return
        pln = ln.getDecLN()
        pln.add(key)
        ln.remove(key)
        self.d[key] = (i-1,pln)
        

    def getMaxKey(self) -> str:
        p = self.tail.prev
        if p.i == 0:
            return ""
        return p.getKey()

    def getMinKey(self) -> str:
        n = self.head.next
        if n.i == 0:
            return ""
        return n.getKey()


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()