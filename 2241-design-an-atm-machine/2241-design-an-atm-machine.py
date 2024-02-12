class ATM:

    def __init__(self):
        self.m = {
            0:20,
            1:50,
            2:100,
            3:200,
            4:500
        }
        self.banknote = [0,0,0,0,0]
        

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.banknote[i] += banknotesCount[i]
        

    def withdraw(self, amount: int) -> List[int]:
        ret = [0,0,0,0,0]
        for i in range(4,-1,-1):
            a = self.m[i]
            cnt = amount//a
            if self.banknote[i] and cnt:
                mn = min(self.banknote[i],cnt)
                ret[i] = mn
                amount -= a*mn
        if amount:
            return [-1]
        for i in range(5):
            self.banknote[i] -= ret[i]
        return ret
            
                


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)