class CustomStack:

    def __init__(self, maxSize: int):
        self.l = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.l)<self.maxSize:
            self.l.append(x)
        
    def pop(self) -> int:
        if not self.l:
            return -1
        return self.l.pop()

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k,len(self.l))):
            self.l[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)