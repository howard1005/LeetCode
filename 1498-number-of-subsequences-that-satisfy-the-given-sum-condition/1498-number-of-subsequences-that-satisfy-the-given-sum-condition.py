from bisect import bisect_right

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        ans = 0
        
        MOD = 1000000007
        
        nums.sort()
        print(nums)
        
        exps = [1]
        for i in range(len(nums)):
            exps.append(exps[-1]*2%MOD)
        
        for i in range(len(nums)):
            n = nums[i]
            j = bisect_right(nums,target-n,0,i)
            ans = (ans + exps[i-j]-1) % MOD
            ans += 1 if n*2 > target else 0
            
        return (exps[len(nums)]-1-ans+MOD)%MOD