class Solution:
    pd = set()
    pl = []
    def findPrimePairs(self, n: int) -> List[List[int]]:
        pd = self.pd
        pl = self.pl
        if not pd:
            for i in range(2,1000000):
                flag = 1
                for j in pl:
                    if j*j > i:
                        break
                    if i%j == 0:
                        flag = 0
                        break
                if flag:
                    pd.add(i)
                    pl.append(i)
        
        ans = []
        for x in pl:
            y = n-x
            if x > y:
                break
            if x in pd and y in pd:
                ans.append((x,y))

        return ans