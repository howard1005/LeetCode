class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        ans = 0

        MOD = 1_000_000_007

        ld,rd = defaultdict(set),defaultdict(set)
        for i,n in enumerate(nums):
            rd[n].add(i)
        for i,n in enumerate(nums):
            rd[n].remove(i)
            lsd,rsd = ld[n*2],rd[n*2]
            ans += len(lsd)*len(rsd)
            ans %= MOD
            ld[n].add(i)
            

        return ans