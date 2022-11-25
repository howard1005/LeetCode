from collections import defaultdict
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        ans = 0
        
        MOD = 1000000007
        
        st = []
        for i,a in enumerate(arr):
            while st and st[-1][1] > a:
                j,b = st.pop()
                k = st[-1][0] if st else -1
                ans = (ans+b*(j-k)*(i-j))%MOD
            st.append((i,a))
        while st:
            j,b = st.pop()
            k = st[-1][0] if st else -1
            ans = (ans+b*(j-k)*(len(arr)-j))%MOD
                
        return ans
            
            
            
            