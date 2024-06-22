class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        
        d = {}
        cum = 0
        for i in range(len(nums)):
            if nums[i]&1:
                cum += 1
            t = cum-k
            if t == 0:
                ans += 1
            if t in d:
                a,b = d[t]
                ans += b-a+1
            if cum not in d:
                d[cum] = [i,i]
            else:
                d[cum][1] = i

        return ans
