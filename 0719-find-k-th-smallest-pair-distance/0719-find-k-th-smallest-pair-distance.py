from bisect import bisect_left,bisect_right

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:

        d = set()
        nums.sort()
        print(nums)
        size = len(nums)
        if k == size*(size-1)//2:
            return nums[-1]-nums[0]
        
        for n in nums:
            d.add(n)

        def near_diff(diff):
            ret = inf
            for i in range(len(nums)):
                n = nums[i]
                t = n-diff
                if t in d:
                    return diff
                lj = bisect_left(nums, t)
                if t not in d and lj-1 >= 0 and lj-1 < len(nums):
                    ret = min(ret, n-nums[lj-1])
            return ret

        def valid(diff):
            lon,hin = 0,0
            for i in range(len(nums)):
                n = nums[i]
                t = n-diff
                lj = bisect_left(nums, t)
                hin += i-lj
                rj = bisect_right(nums, t)
                lon += i-rj
            if lon+1 <= k and k <= hin+1:
                return 0
            elif k < lon+1:
                return -1
            else:
                return 1


        lo,hi = 0,nums[-1]-nums[0]
        while lo<=hi:
            mi = (lo+hi)//2
            res = valid(mi)
            if res == 1:
                lo = mi + 1
            elif res == -1:
                hi = mi - 1
            else:
                return near_diff(mi)
            
        return -1
