import random

class RandomizedSet:

    def __init__(self):
        self.d = {}
        self.l = []
        

    def insert(self, val: int) -> bool:
        if not val in self.d:
            self.d[val] = len(self.l)
            self.l.append(val)
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.d:
            idx = self.d[val]
            n = self.l[-1]
            self.l[idx] = n
            self.d[n] = idx
            del self.d[val]
            self.l.pop()
            return True
        return False
        

    def getRandom(self) -> int:
        return random.choice(self.l)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()