class Solution:
    ansl = [-1 for _ in range(10001)]
    def rotatedDigits(self, n: int) -> int:
        if self.ansl[0] == -1:
            self.ansl[0] = 0
            invd = set(['3','4','7'])
            vd = set(['2','5','6','9'])
            cum = 0
            for i in range(1,10001):
                sd = set(str(i))
                if sd & invd:
                    pass
                elif sd & vd:
                    cum += 1
                self.ansl[i] = cum
        return self.ansl[n]