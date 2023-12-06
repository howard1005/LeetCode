class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        
        t = 0
        o = 1
        while n:
            ans += t + o
            n -= 1
            t += 1
            if t == 7:
                t = 0
                o += 1
            
        return ans
            
            