from bisect import bisect_left as bl

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        a = []
        for n in nums:
            i = bl(a,n)
            if len(a) == i:
                a.append(n)
            else:
                a[i] = n
        return len(a)
                
            
                