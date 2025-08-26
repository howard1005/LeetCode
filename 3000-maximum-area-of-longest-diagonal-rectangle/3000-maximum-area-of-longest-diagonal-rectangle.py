class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        ans = 0
        mxdig = 0

        for a,b in dimensions:
            dig = a*a+b*b
            if mxdig < dig:
                ans = a*b
                mxdig = dig
            elif mxdig == dig:
                ans = max(ans,a*b)

        return ans