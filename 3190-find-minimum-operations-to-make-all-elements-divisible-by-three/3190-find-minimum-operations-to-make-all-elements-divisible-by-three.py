class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0

        for n in nums:
            m = n%3
            ans += min(m,3-m)

        return ans