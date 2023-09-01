class Solution:
    ans = []
    def countBits(self, n: int) -> List[int]:
        if not self.ans:
            for i in range(10**5+1):
                cnt = 0
                while i:
                    if i&1:
                        cnt+=1
                    i >>= 1
                self.ans.append(cnt)
        return self.ans[:n+1]