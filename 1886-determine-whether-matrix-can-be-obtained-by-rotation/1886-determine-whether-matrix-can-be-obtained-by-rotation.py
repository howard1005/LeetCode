class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        m,n = len(mat),len(mat[0])
        def rot(mat):
            ret = [[0 for _ in range(n)] for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    ret[j][m-i-1] = mat[i][j]
            return ret

        def valid(mat,target):
            for i in range(m):
                for j in range(n):
                    if mat[i][j] != target[i][j]:
                        return False
            return True
        
        for _ in range(4):
            # print(_)
            # for r in mat:
            #     print(r)
            if valid(mat,target):
                return True
            mat = rot(mat)

        return False
            