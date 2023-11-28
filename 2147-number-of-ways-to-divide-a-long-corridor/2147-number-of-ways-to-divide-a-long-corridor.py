class Solution:
    def numberOfWays(self, corridor: str) -> int:        
        MOD = 1000000007
        
        l = []
        
        for i in range(len(corridor)):
            if corridor[i] == 'S':
                l.append(i)
        
        if len(l)%2 == 1:
            return 0
        elif len(l) == 0:
            return 0
        
        t = 1
        for i in range(1,len(l)-1,2):
            t *= l[i+1]-l[i]
            t %= MOD
            
        return t
        
        