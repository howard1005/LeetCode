class Solution:
    def countBalancedPermutations(self, num: str) -> int:

        MOD = 1_000_000_007

        l = [int(n) for n in num]

        if sum(l)&1:
            return 0

        d = defaultdict(int)

        for n in l:
            d[n] += 1

        @cache
        def fact(n):
            if n <= 1:
                return 1
            return (n * fact(n-1))%MOD

        @cache
        def inv_fact(n):
            if n <= 1:
                return 1
            return pow(fact(n),MOD-2,MOD)

        tcnt = len(l)//2 + (1 if len(l)&1 else 0)
        tcum = sum(l)//2

        per = (fact(tcnt)*fact(len(l)-tcnt))%MOD

        @cache
        def dfs(i,cnt,cum):
            if i == 10:
                if cnt == tcnt and cum == tcum:
                    return per
                return 0

            ret = 0

            for j in range(d[i]+1):
                ret += (dfs(i+1,cnt+j,cum+i*j) * inv_fact(j) * inv_fact(d[i]-j))%MOD
                ret %= MOD

            return ret

        ans = dfs(0,0,0)

        return ans