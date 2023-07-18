class LRUCache:

    def __init__(self, capacity: int):
        self.dq = deque()
        self.d = {}
        self.tick = 0
        self.c = capacity

    def get(self, key: int) -> int:
        self.tick += 1
        if key in self.d:
            v,t = self.d[key]
            self.d[key] = (v,self.tick)
            self.dq.append((key,self.tick))
            return v
        return -1

    def put(self, key: int, value: int) -> None:
        self.tick += 1
        if key not in self.d and len(self.d) == self.c:
            self.removeOld()
        self.d[key] = (value,self.tick)
        self.dq.append((key,self.tick))
        
    def removeOld(self):
        while self.dq:
            k,t = self.dq.popleft()
            if k in self.d and self.d[k][1] == t:
                del self.d[k]
                break
                
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)