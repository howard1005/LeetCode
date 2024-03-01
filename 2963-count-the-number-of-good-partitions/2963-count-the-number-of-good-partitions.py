class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        MOD = 1000000007
        
        ans = 0
        
        d = {}
        
        for i,n in enumerate(nums):
            if n not in d:
                d[n] = [i,i]
            else:
                d[n][1] = i
                
        l = [[v[0],v[1],k] for k,v in d.items()]
        l.sort()
        
        def intersection(a1,b1,a2,b2):
            return [max(a1,a2),min(b1,b2)]
        
        
        st = [l[0]]
        for a1,b1,v1 in l[1:]:
            a2,b2,v2 = st[-1]
            it = intersection(a1,b1,a2,b2)
            if it[0]<=it[1]:
                st[-1][1] = max(b1,b2)
            else:
                st.append([a1,b1,v1])
        
        ans = 1
        for _ in range(len(st)-1):
            ans = ans*2%MOD
        
        return ans

        
        
        
        
        