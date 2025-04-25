class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        ans = 0

        l = []

        for n in nums:
            m = n%modulo
            t = 1 if m == k else 0
            l.append(t)
            if len(l)>1:
                l[-1] += l[-2]
        
        d = defaultdict(int)

        for cum in l:
            m = cum%modulo
            if m == k:
                ans += 1
            t = (m-k+modulo)%modulo
            ans += d[t]
            d[m] += 1
        
        return ans