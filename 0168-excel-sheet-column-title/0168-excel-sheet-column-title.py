class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ''
        s = 'ZABCDEFGHIJKLMNOPQRSTUVWXY'
        
        exp = 26
        n = columnNumber
        l = []
        while n:
            l.append(s[n%exp])
            o = 1 if n%exp == 0 else 0
            n = n//exp - o
            
        
        l.reverse()
        ans = ''.join(l)
            
        return ans