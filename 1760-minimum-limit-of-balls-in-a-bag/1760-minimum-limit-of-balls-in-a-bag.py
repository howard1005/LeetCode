class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:

        nums.sort(reverse=True)

        def valid(t):
            o = maxOperations
            for n in nums:
                if n <= t:
                    break
                m = n//t - (1 if n%t == 0 else 0)
                print(t,n,m)
                o -= m
                if o < 0:
                    return False
            return True

        ans = inf

        lo,hi = 1,1000000000
        while lo<=hi:
            mi = (lo+hi)//2
            if valid(mi):
                ans = min(ans,mi)
                hi = mi - 1
            else:
                lo = mi + 1

        return ans
                

