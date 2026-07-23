class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        ans = 0

        n = len(nums)

        if n == 1:
            return 1
        if n == 2:
            return 2

        x = 0
        while n:
            x+=1
            n>>=1

        ans = 1<<(x+1)-1

        return ans