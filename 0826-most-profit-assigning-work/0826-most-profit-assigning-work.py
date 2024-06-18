from bisect import bisect_right

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        ans = 0
        
        l = [(d,p) for d,p in zip(difficulty,profit)]
        l.sort()

        mxl = [0 for _ in range(len(difficulty))]
        mxl[0] = l[0][1]
        for i in range(1,len(l)):
            mxl[i] = max(mxl[i-1],l[i][1])

        # print(l)
        # print(mxl)
        for w in worker:
            i = bisect_right(l,w,key=lambda x:x[0])-1
            # print(w,i,mxl[i])
            if i >= 0:
                ans += mxl[i]

        return ans