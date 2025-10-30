class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ans = 0

        st = []

        for i,v in enumerate(target):
            while st and st[-1][1] >= v:
                ii,vv = st.pop()
                diff = vv-(max(st[-1][1],v) if st else v)
                ans += diff
            st.append((i,v))
        
        while st:
            ii,vv = st.pop()
            diff = vv-(st[-1][1] if st else 0)
            ans += diff

        return ans