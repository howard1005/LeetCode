class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n:
            return []

        ansl = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                ansl[i][j] = original[i*n+j]

        return ansl