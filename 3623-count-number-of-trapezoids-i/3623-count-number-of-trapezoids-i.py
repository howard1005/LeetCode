class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        ans = 0

        MOD = 1_000_000_007

        d = defaultdict(int)

        for _,y in points:
            d[y] += 1

        cum = 0
        for n in d.values():
            cnt = n*(n-1)//2
            ans += cum*cnt
            ans %= MOD
            cum += cnt


        return ans