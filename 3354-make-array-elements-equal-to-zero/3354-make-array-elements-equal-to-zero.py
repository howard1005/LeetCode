class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        ll = nums[:]
        rl = nums[:]

        for i in range(1,len(ll)):
            ll[i] += ll[i-1]
        for i in range(len(rl)-2,-1,-1):
            rl[i] += rl[i+1]

        ans = 0

        for i in range(len(nums)):
            v = nums[i]
            if v == 0:
                l,r = ll[i],rl[i]
                if l-r == 0 or l-r ==1:
                    ans += 1
                if r-l == 0 or r-l ==1:
                    ans += 1

        return ans