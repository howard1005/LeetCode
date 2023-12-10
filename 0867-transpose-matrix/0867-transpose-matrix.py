class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m,n = len(matrix),len(matrix[0])
        ansl = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                ansl[j][i] = matrix[i][j]
        return ansl