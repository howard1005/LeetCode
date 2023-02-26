class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        ans = [[0]*len(colsum),[0]*len(colsum)]
        
        for i,cs in enumerate(colsum):
            if cs == 2:
                ans[0][i] = 1
                ans[1][i] = 1
                upper -= 1
                lower -= 1
        for i,cs in enumerate(colsum):
            if cs == 1:
                if upper > 0:
                    ans[0][i] = 1
                    upper -= 1
                elif lower > 0 :
                    ans[1][i] = 1
                    lower -= 1
                else:
                    return []
                
        if upper == 0 and lower == 0:
            return ans
        
        return []