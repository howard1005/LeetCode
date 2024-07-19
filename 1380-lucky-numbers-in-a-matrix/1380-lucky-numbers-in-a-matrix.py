class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        sdr,sdc = set(),set()

        for r in matrix:
            sdr.add(min(r))

        for j in range(len(matrix[0])):
            mx = 0
            for i in range(len(matrix)):
                mx = max(mx,matrix[i][j])
            sdc.add(mx)
        
        return sdr&sdc