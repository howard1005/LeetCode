class LFUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.dd = defaultdict(deque)
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.d:
            self.d[key][1] += 1
            self.dd[self.d[key][1]].append(key)
            return self.d[key][0]
        return -1

    def popLFU(self):
        for i in range(1,len(self.dd)+1):
            dq = self.dd[i]
            while dq:
                k = dq.popleft()
                if k in self.d and self.d[k][1] == i:
                    del self.d[k]
                    return
            
    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        if key in self.d:
            self.d[key][0] = value
            self.get(key)
            return
        if len(self.d) == self.cap:
            self.popLFU()
        self.d[key] = [value,1]
        self.dd[1].append(key)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)