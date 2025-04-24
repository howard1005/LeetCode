class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        ans = 0

        d = defaultdict(int)

        i,j = 0,0
        
        size = len(set(nums))

        while j<len(nums):
            n = nums[j]
            d[n] += 1
            while i<j:
                m = nums[i]
                if d[m] == 1:
                    break
                d[m] -= 1
                i += 1
            if len(d) == size:
                ans += i+1
            j += 1

        return ans