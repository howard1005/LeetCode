from heapq import heappush,heappop

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        ans = inf

        cuml = [0 for _ in range(len(nums))]
        cuml[0] = nums[0]
        for i in range(1,len(nums)):
            cuml[i] += cuml[i-1]+nums[i]

        l = [(i,e) for i,e in enumerate(cuml)]
        l.sort(key=lambda x: -x[1])
        # print(l)

        h = []
        for i,e in l:
            heappush(h,(-i,e))

        for i,e in l:
            q = e-k
            if e >= k:
                ans = min(ans,i+1)
            while h and h[0][1] > q:
                heappop(h)
            # print(i,e,q,h)
            if h:
                length = i+h[0][0]
                if length > 0:
                    ans = min(ans,length)

        return ans if ans != inf else -1