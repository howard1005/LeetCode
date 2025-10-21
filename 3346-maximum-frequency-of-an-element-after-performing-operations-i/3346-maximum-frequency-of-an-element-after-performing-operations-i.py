from bisect import bisect_left,bisect_right

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        ans = 0

        nums.sort()

        d = defaultdict(int)

        for n in nums:
            d[n] += 1

        for n in nums:
            a = bisect_left(nums,n-k)
            b = bisect_right(nums,n+k)
            ans = max(ans,min(b-a,numOperations+d[n]))


        for i,n in enumerate(nums):
            m = n+2*k
            j = bisect_right(nums,m,i,len(nums))
            ans = max(ans,min(j-i,numOperations))

        return ans
