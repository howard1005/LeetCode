class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        ans = -inf
        
        l = []
        f = 0
        hi = 0
        for i in range(len(nums)-1):
            a,b = nums[i],nums[i+1]
            if a<b:
                if f == 1:
                    pass
                elif f == -1:
                    l.append((hi,i,-1))
                    hi = i
                    f = 1
                else:
                    hi = i
                    f = 1
            elif a>b:
                if f == 1:
                    l.append((hi,i,1))
                    hi = i
                    f = -1
                elif f == -1:
                    pass
                else:
                    hi = i
                    f = -1
            else:
                if f == 1:
                    l.append((hi,i,1))
                    hi = i+1
                    f = 0
                elif f == -1:
                    l.append((hi,i,-1))
                    hi = i+1
                    f = 0
                else:
                    hi = i+1
        if f != 0:
            l.append((hi,len(nums)-1,f))

        # print(l)

        cuml = nums[:]
        for i in range(1,len(cuml)):
            cuml[i] += cuml[i-1]

        # print(cuml)
        
        def cal(i,j):
            if i>j:
                return 0
            return cuml[j]-(cuml[i-1] if i-1>=0 else 0)

        mxl = [[-inf,-inf] for _ in range(len(l))]
        for idx in range(len(l)):
            i,j,f = l[idx]

            lmx = -inf
            cum = nums[i]
            for ii in range(i+1,j+1):
                cum += nums[ii]
                lmx = max(lmx,cum)
            mxl[idx][0] = lmx

            rmx = -inf
            cum = nums[j]
            for ii in range(j-1,i-1,-1):
                cum += nums[ii]
                rmx = max(rmx,cum)
            mxl[idx][1] = rmx

        # print('mxl',mxl)

        for idx in range(len(l)-2):
            i1,j1,f1 = l[idx]
            i2,j2,f2 = l[idx+1]
            i3,j3,f3 = l[idx+2]
            
            if f1 != 1:
                continue

            if j1 != i2 or j2 != i3:
                continue

            t = mxl[idx][1] + cal(i2+1,j2-1) + mxl[idx+2][0]

            ans = max(ans,t)
            
            

        return ans
                    