class Solution:
    def kthGrammar(self, n: int, k: int) -> int:       
        d = {}
        nn,kk = n-1,k-1
        while nn>=0:
            d[nn] = kk
            nn -= 1
            kk //= 2
        
        s = '0'
        for i in range(n):
            c = s[d[i]%2]
            if c == '0':
                s = '01'
            else:
                s = '10'
        
        return int(s[0])