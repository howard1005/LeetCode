class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        ans = 0

        for kk in range(k):
            d = defaultdict(int)
            for n in nums:
                m = n%k
                t = (kk-m+k)%k
                d[m] = max(d[m],d[t]+1)
                ans = max(ans,d[m])
            # print(kk,d)
        
        return ans