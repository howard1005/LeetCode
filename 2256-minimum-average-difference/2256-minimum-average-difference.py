class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        ans = -1
        
        ad = inf
        tot = sum(nums)
        cum = 0
        for i in range(len(nums)-1):
            cum += nums[i]
            a1 = int(cum/(i+1))
            a2 = int((tot-cum)/(len(nums)-i-1))
            ad_ = abs(a1-a2)
            if ad > ad_:
                ans = i
                ad = ad_
        ad_ = int(tot/len(nums))
        if ad > ad_:
            ans = len(nums)-1
            ad = ad_
        
        return ans