from bisect import bisect_left,bisect_right

class Solution:
    l = []
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        if not self.l:
            for length in range(1,10):
                for i in range(1,10):
                    if i+length<=10:
                        n = 0
                        for j in range(i,i+length):
                            n = n*10 + j
                        self.l.append(n)         
        return self.l[bisect_left(self.l,low):bisect_right(self.l,high)]
        