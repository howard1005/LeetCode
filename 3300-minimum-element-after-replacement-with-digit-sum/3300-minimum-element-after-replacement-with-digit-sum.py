class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = inf

        for n in nums:
            t = 0
            while n:
                t += n%10
                n //= 10
            ans = min(ans,t)

        return ans