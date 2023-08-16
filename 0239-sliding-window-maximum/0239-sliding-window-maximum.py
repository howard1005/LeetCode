from heapq import heappush,heappop

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        
        hq = []
        
        i,j = 0,0
        for _ in range(k):
            heappush(hq,(-nums[j],j))
            j += 1
        ans.append(-hq[0][0])
        
        while j < len(nums):
            i += 1
            while hq and hq[0][1] < i:
                heappop(hq)
            heappush(hq,(-nums[j],j))
            j += 1
            ans.append(-hq[0][0])
            
        return ans
        
        
        