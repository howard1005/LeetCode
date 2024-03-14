class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans = 0
        
        d = defaultdict(int)
        cum = 0
        for n in nums:
            cum += n
            d[cum] += 1
        
        ans += d[goal]
        
        for i in list(d.keys()):
            j = i+goal
            if i == j:
                ans += d[i]*(d[i]-1)//2
            else:
                ans += d[i]*d[j]
            
        return ans