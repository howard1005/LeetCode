class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        ans = 0

        m,n = len(mat),len(mat[0])

        cmat = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            cnt = 0
            for j in range(n):
                if mat[i][j]:
                    cnt += 1
                else:
                    cnt = 0
                cmat[i][j] = cnt

        # for r in cmat:
        #     print(r) 
        
        
        for j in range(n):
            st = [(-1,-1,-1)] # (i, 두께, 길이(가장 last와의 diff))
            cum = 0
            for i in range(m):
                v = cmat[i][j]

                # print(f"{i},{j},{v} before {st} {cum}")

                while st[-1][1]>=v:
                    pt = st.pop()
                    cum -= pt[1]*pt[2]
                
                t = (i,v,i-st[-1][0])
                cum += t[1]*t[2]

                st.append(t)

                # print(f"{i},{j},{v} after {st} {cum}")

                ans += cum


        return ans

                

