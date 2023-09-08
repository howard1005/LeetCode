class Solution:
    ans = []
    def generate(self, numRows: int) -> List[List[int]]:
        if not self.ans:
            self.ans.append([1])
            i = 1
            while i <= 30:
                tmp = [1]
                l = self.ans[-1]
                for i in range(len(l)-1):
                    tmp.append(l[i]+l[i+1])
                tmp.append(1)
                self.ans.append(tmp)
                i += 1
        
        return self.ans[:numRows]