from heapq import heappush,heappop

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ans = 0

        def toplazy(i,h):
            while h and h[0][1]<i:
                heappop(h)
            return h[0]

        mxhq,mnhq = [],[]

        i,j = 0,0
        while j<len(nums):
            heappush(mxhq,(-nums[j],j))
            heappush(mnhq,(nums[j],j))

            while i<=j and mxhq and abs(toplazy(i,mxhq)[0]+toplazy(i,mnhq)[0])>limit:
                i+=1
                
            ans = max(ans,j-i+1)
            j+=1

        return ans