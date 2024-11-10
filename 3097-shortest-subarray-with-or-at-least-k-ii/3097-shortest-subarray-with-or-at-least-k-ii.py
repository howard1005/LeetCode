class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = inf

        d = defaultdict(int)

        def get_cum():
            ret = 0
            for k,v in d.items():
                if v:
                    ret |= (1<<k)
            return ret   

        def patch(n,op):
            i = 0
            while n:
                if n&1:
                    d[i] += op
                n >>= 1
                i += 1
        
        j = 0
        for i in range(len(nums)):
            patch(nums[i],1)
            while j<i:
                patch(nums[j],-1)
                if get_cum() < k:
                    patch(nums[j],1)
                    break
                j += 1
            if get_cum() >= k:
                ans = min(ans,i-j+1)
        
        return ans if ans != inf else -1