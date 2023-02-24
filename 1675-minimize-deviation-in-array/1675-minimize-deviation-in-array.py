import heapq

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        def get_min(n):
            while not n&1:
                n>>=1
            return n
        h = []
        mx,mn = -float('inf'),float('inf')
        for n in nums:
            if n&1:
                heapq.heappush(h,(n,n*2))
                mx = max(mx, n)
                mn = min(mn, n)
            else:
                nn = get_min(n)
                heapq.heappush(h,(nn,n))
                mx = max(mx, nn)
                mn = min(mn, nn)
        ans = float('inf')
        while 1:
            n,limit = heapq.heappop(h)
            mn = n
            ans = min(ans, mx-mn)
            if n*2 <= limit:
                mx = max(mx, n*2)
                heapq.heappush(h,(n*2,limit))
            else:
                break
        return ans
            

        