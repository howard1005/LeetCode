class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        l1 = [int(c) for c in str(num1)]
        l2 = [int(c) for c in str(num2)]
        l1 = [0]*(len(l2)-len(l1))+l1
        
        # dp[i][prevN][equal,dec,inc][lo][hi]
        
        @cache
        def dfs(i,prevN,di,lof,hif):
            # print(i,prevN,di,lof,hif)
            if i >= len(l2):
                return 0,1
            ret = 0
            rcnt = 0
            lo = l1[i] if lof else 0
            hi = l2[i] if hif else 9
            for n in range(lo,hi+1):
                exist = 0
                if prevN != -1 and prevN < n and di == 1:
                    # print('valleys',i,prevN,di,lof,hif)
                    exist = 1
                if prevN != -1 and prevN > n and di == 2:
                    # print('peaks',i,prevN,di,lof,hif)
                    exist = 1

                ndi = di
                if prevN == 0 or prevN == n:
                    ndi = 0
                if prevN != -1 and prevN > n:
                    ndi = 1
                if prevN != -1 and prevN < n:
                    ndi = 2
                
                nlof = lof
                if n > lo:
                    nlof = 0
                nhif = hif
                if n < hi:
                    nhif = 0
                nn = -1 if prevN == -1 and n == 0 else n
                nret,nrcnt = dfs(i+1,nn,ndi,nlof,nhif)
                ret += nret + exist*nrcnt
                rcnt += nrcnt

            return ret,rcnt

        ans,_ = dfs(0,-1,0,1,1)

        return ans
                



        
        