class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        ans = -1

        if len(nums) == k:
            return max(nums)

        d = defaultdict(int)
        for n in nums:
            d[n] += 1

        if k == 1:
            for k,v in d.items():
                if v == 1:
                    ans = max(ans,k)
            return ans
        
        if d[nums[0]] == 1:
            ans = max(ans,nums[0])
        if d[nums[-1]] == 1:
            ans = max(ans,nums[-1])
        
        return ans