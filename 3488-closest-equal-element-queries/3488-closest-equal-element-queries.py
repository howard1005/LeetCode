from bisect import bisect_left

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        ans = [inf for _ in range(len(queries))]

        d = defaultdict(list)
        for i,n in enumerate(nums):
            d[n].append(i)

        for i,q in enumerate(queries):
            l = d[nums[q]]

            if len(l) < 2:
                continue

            j = bisect_left(l,q)

            # print(i,q,j,l)

            
            dis = abs(l[(j+1)%len(l)]-q)
            ans[i] = min(ans[i],dis,len(nums)-dis)
            dis = abs(l[(j-1+len(l)%len(l))]-q)
            ans[i] = min(ans[i],dis,len(nums)-dis)
            

        for i,a in enumerate(ans):
            if ans[i] == inf:
                ans[i] = -1

        return ans