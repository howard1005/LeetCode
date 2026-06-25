class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        ans = 0

        sl = SortedList()

        l = []
        cum = 0
        for i,n in enumerate(nums):
            if n == target:
                cum += 1
            else:
                cum -= 1
            l.append(cum)

        for i,c in enumerate(l):
            if c > 0:
                ans += 1
            j = sl.bisect_left(c)
            ans += j
            sl.add(c)
            
        return ans