class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        l = [(i,arr[0],arr[-1]) for i,arr in enumerate(arrays)]

        mnl = list(sorted(l,key=lambda x: x[1]))
        mxl = list(sorted(l,key=lambda x: -x[2]))

        if mnl[0][0] != mxl[0][0]:
            return mxl[0][2]-mnl[0][1]
        
        return max(mxl[0][2]-mnl[1][1],mxl[1][2]-mnl[0][1])