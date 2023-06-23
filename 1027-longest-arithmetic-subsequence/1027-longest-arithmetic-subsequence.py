class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        ans = 0
        
        diff = max(nums)-min(nums)
        d = defaultdict(int)
        for n in nums:
            for t in range(-diff,diff+1):
                d[(n,t)] = d[((n+t,t))]+1
                ans = max(ans,d[(n,t)])
                
        return ans
                    
                