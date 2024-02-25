class Solution:
    pl = []
    pd = defaultdict(list)
    
    def initP(self):
        pl = self.pl
        pd = self.pd
        def isPrime(n):
            i = 2
            while i*i <= n:
                if n%i == 0:
                    return False
                i += 1
            return True
        
        if not pd:
            for i in range(2,100001):
                if isPrime(i):
                    pl.append(i)
            
            for p in pl:
                i = 1
                while p*i < 100001:
                    pd[p*i].append(p)
                    i += 1
        return pl,pd
        
    
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        for n in nums:
            if n == 1:
                return False
        
        pl,pd = self.initP()
        
        pars = {}
        
        def findPar(i):
            if i not in pars:
                pars[i] = i
            tl = []
            while i != pars[i]:
                tl.append(i)
                i = pars[i]
            for ii in tl:
                pars[ii] = i
            return i
        
        def union(i,j):
            pi,pj = findPar(i),findPar(j)
            pars[pj] = pi
                    
        
        for n in nums:
            l = pd[n]
            for i in range(len(l)-1):
                union(l[i],l[i+1])
        
        t = findPar(pd[nums[0]][0])
        for n in nums:
            if t != findPar(pd[n][0]):
                return False

        return True

        
        
        
        
            