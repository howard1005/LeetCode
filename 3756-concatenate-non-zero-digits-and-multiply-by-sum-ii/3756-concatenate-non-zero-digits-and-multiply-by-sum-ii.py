class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        ans = []

        MOD = 10**9+7

        decs = [1]
        for _ in range(len(s)):
            decs.append(decs[-1]*10%MOD)
        # print(decs)

        cuml1 = [int(s[0])]
        for i in range(1,len(s)):
            n = int(s[i])
            cuml1.append(cuml1[-1]+n)
        # print(cuml1)
        def sumq(i,j):
            return cuml1[j]-(cuml1[i-1] if i-1>=0 else 0)

        cuml2 = [(int(s[0]),0 if s[0] == '0' else 1)]
        for i in range(1,len(s)):
            n = int(s[i])
            px,psize = cuml2[-1]
            if n != 0:
                cuml2.append(((px*10+n)%MOD,psize+1))
            else:
                cuml2.append((px,psize))
        # print(cuml2)
        def xq(i,j):
            px,psize = (cuml2[i-1] if i-1>=0 else (0,0))
            x,size = cuml2[j]
            px = px*decs[size-psize]%MOD
            return (x-px+MOD)%MOD
        # print(xq(1,3))

        for i,j in queries:
            ans.append(sumq(i,j)*xq(i,j)%MOD)

        return ans