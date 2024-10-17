class Solution:
    def maximumSwap(self, num: int) -> int:
        ans = 0
        
        sl = list(str(num))

        def proc():
            for i,c in enumerate(sl):
                n = int(c)
                for j in range(9,n,-1):
                    cj = str(j)
                    for k in range(len(sl)-1,i,-1):
                        if sl[k] == cj:
                            return i,k
            return -1,-1
        
        i,k = proc()
        if i == -1:
            return num

        
        sl[i],sl[k] = sl[k],sl[i]

        ans = int(''.join(sl))

        return ans