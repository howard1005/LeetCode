class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = {0:-1}

        cum = 0
        for i,n in enumerate(nums):
            cum += n
            m = cum%k
            if m in d and i-d[m]>=2:
                return True
            if m in d:
                d[m] = min(d[m],i)
            else:
                d[m] = i

        return False 