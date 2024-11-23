class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:

        m,n = len(box),len(box[0])

        ret = [['.' for _ in range(m)] for _ in range(n)]

        # i,j -> j,m-i-1
        for i in range(m):
            for j in range(n):
                ret[j][m-i-1] = box[i][j]

        def upstack(cnt,i,j):
            for ii in range(i-1,i-cnt-1,-1):
                ret[ii][j] = '#'

        for j in range(m):
            cnt = 0
            for i in range(n):
                c = ret[i][j]
                if c == '#':
                    cnt += 1
                    ret[i][j] = '.'
                if c == '*':
                    upstack(cnt,i,j)
                    cnt = 0
            if cnt:
                upstack(cnt,n,j)

        return ret