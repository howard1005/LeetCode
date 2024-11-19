class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans = 0

        d = defaultdict(int)
        cum = 0
        dup = 0

        i,j = 0,0
        while j < k:
            n = nums[j]
            d[n] += 1
            cum += n
            if d[n] == 2:
                dup += 1
            j += 1
        if not dup:
            ans = max(ans,cum)
        
        while j < len(nums):
            n1 = nums[i]
            d[n1] -= 1
            cum -= n1
            if d[n1] == 1:
                dup -= 1

            n2 = nums[j]
            d[n2] += 1
            cum += n2
            if d[n2] == 2:
                dup += 1

            if not dup:
                ans = max(ans,cum)
            i += 1
            j += 1

        return ans