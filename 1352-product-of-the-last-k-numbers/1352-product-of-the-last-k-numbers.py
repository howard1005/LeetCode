class ProductOfNumbers:

    def __init__(self):
        self.l = []
        self.zi = -1

    def add(self, num: int) -> None:
        l = self.l
        if num == 0:
            self.zi = len(l)
            if l:
                l.append(l[-1])
            else:
                l.append(1)
            return
        
        if l:
            l.append(l[-1]*num)
        else:
            l.append(num)

    def getProduct(self, k: int) -> int:
        # print(self.l,k,self.zi)
        if len(self.l)-k <= self.zi:
            return 0
        return self.l[-1]//(self.l[-k-1] if k+1 <= len(self.l) else 1)


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)