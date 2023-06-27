from heapq import heappush,heappop

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans = []
        
        hq = []
        for i,n in enumerate(nums1):
            heappush(hq,(n+nums2[0],i,0))
            
        for _ in range(k):
            if not hq:
                break
            v,i,j = heappop(hq)
            ans.append([nums1[i],nums2[j]])
            if j+1 < len(nums2):
                heappush(hq,(nums1[i]+nums2[j+1],i,j+1))
        
        return ans