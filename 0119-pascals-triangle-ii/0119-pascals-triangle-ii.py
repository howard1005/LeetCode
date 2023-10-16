class Solution:
    tl = []
    def getRow(self, rowIndex: int) -> List[int]:
        tl = self.tl
        if not tl:
            tl.append((1,))
            for _ in range(33):
                p = tl[-1]
                c = [1]
                for i in range(len(p)-1):
                    c.append(p[i]+p[i+1])
                c.append(1)
                tl.append(tuple(c))                    
            
        return tl[rowIndex]