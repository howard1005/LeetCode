class Solution:
    pl = []
    def countPermutations(self, complexity: List[int]) -> int:
        ans = 0

        MOD = 1_000_000_007

        if not self.pl:
            self.pl.append(1)
            for i in range(1,100001):
                self.pl.append(self.pl[-1]*i%MOD)

        mn = inf
        d = defaultdict(int)
        for c in complexity:
            mn = min(mn,c)
            d[c] += 1
        if mn != complexity[0] or d[mn] >= 2:
            return 0

        ans = self.pl[len(complexity)-1]

        return ans