class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        ans = []

        MOD = 1_000_000_007

        powers = []
        
        i = 0
        while n:
            if n&1:
                powers.append(2**i)
            i += 1
            n >>= 1

        @cache
        def query(i,j):
            ret = 1
            for a in range(i,j+1):
                ret = ret*powers[a]%MOD
            return ret
        
        for i,j in queries:
            ans.append(query(i,j))


        return ans