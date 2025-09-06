class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        ans = 0

        for a,b in queries:
            cnt = 0
            for i in range(16):
                c = 1<<(i*2)
                d = (c<<2)-1

                if b < c:
                    break
                    
                e,f = max(a,c),min(b,d)

                if e > f:
                    continue

                cnt += (i+1)*(f-e+1)

            ans += cnt//2 + (cnt&1)

        return ans