class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        ans = inf

        d = defaultdict(int)

        tm = sum(nums)%p
        if tm == 0:
            return 0

        cum = 0
        for i,n in enumerate(nums):
            cum += n
            m = cum%p
            fm = (m-tm+p)%p
            if fm == 0:
                ans = min(ans,i+1)
            if fm in d:
                j = d[fm]
                ans = min(ans,i-j)
            d[m] = i

        return -1 if ans == len(nums) else ans