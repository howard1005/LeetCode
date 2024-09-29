class AllOne:

    def __init__(self):
        self.d = defaultdict(int)
        self.rd = defaultdict(set)
        self.maxi = 0
        self.mini = 0

    def _update(self):
        for i in range(self.maxi+1,self.maxi-2,-1):
            if i>0 and self.rd[i]:
                self.maxi = i
                break
        for i in range(self.mini-1,self.mini+2):
            if i>0 and self.rd[i]:
                self.mini = i
                break

    def inc(self, key: str) -> None:
        i = self.d[key]
        if key in self.rd[i]:
            self.rd[i].remove(key)
        self.rd[i+1].add(key)
        self.d[key] += 1
        self._update()
        

    def dec(self, key: str) -> None:
        i = self.d[key]
        if key in self.rd[i]:
            self.rd[i].remove(key)
        self.rd[i-1].add(key)
        self.d[key] -= 1
        self._update()
        

    def getMaxKey(self) -> str:
        if not self.rd[self.maxi]:
            return ""
        sd = self.rd[self.maxi]
        ret = sd.pop()
        sd.add(ret)
        return ret
        

    def getMinKey(self) -> str:
        if not self.rd[self.mini]:
            return ""
        sd = self.rd[self.mini]
        ret = sd.pop()
        sd.add(ret)
        return ret


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()