from heapq import heappush,heappop

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        
        t1,t2 = sum(nums1),sum(nums2)
        if t1 > t2:
            t1,t2 = t2,t1
            nums1,nums2 = nums2,nums1
        
        diff = t2-t1
        hq = []
        for n in nums1:
            heappush(hq,-(6-n))
        for n in nums2:
            heappush(hq,-(n-1))
            
        while diff and hq:
            dt = heappop(hq)
            ans += 1
            if diff + dt < 0:
                diff = 0
                break
            diff += dt
            
        return ans if diff == 0 else -1