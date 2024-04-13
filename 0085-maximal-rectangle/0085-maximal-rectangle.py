class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m,n = len(matrix),len(matrix[0])
        mp = [[0 for _ in range(n)] for _ in range(m)]
        for j in range(n):
            for i in range(m):
                if matrix[i][j] == '1':
                    mp[i][j]+=1
                    if i>0:
                        mp[i][j]+=mp[i-1][j]
        #for r in mp:
        #    print(r)
        
        ans = 0
        def proc(l):
            nonlocal ans
            st = []
            for i,h in enumerate(l):
                #print(ans,st)
                ii = i
                if st:
                    jj = i-1
                    while st and st[-1][1]>h:
                        ii,hh = st.pop()
                        ans = max(ans,(jj-ii+1)*hh)
                if h:
                    st.append((ii,h))
            if st:
                jj = len(l)-1
                while st:
                    #print(ans,st)
                    ii,hh = st.pop()
                    ans = max(ans,(jj-ii+1)*hh)
                    
        for r in mp:
            proc(r)
        
        return ans