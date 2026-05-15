class Solution:
    def findMin(self, nums: List[int]) -> int:
        p = nums[-1]
        ans = p
        l,r = 0,len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m] < p:
                r = m-1
                ans = nums[m]
            else:
                l = m+1
                
        return ans