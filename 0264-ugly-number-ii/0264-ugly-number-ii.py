class Solution:
    uglies = []
    def nthUglyNumber(self, n: int) -> int:
        def ugliesUnder(num):
            l = []
            for a in range(32):
                an = 2**a
                if an>num:break
                for b in range(32):
                    bn = 3**b
                    if an*bn>num:break
                    for c in range(32):
                        cn = 5**c
                        if an*bn*cn>num:break
                        l.append(an*bn*cn)
            return l

        if not self.uglies:
            self.uglies = ugliesUnder(2123366400)
            self.uglies.sort()

        return self.uglies[n-1]
                
            