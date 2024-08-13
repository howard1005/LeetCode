class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[set() for _ in range(target+1)] for _ in range(len(candidates))]
        for j in range(target+1):
            n = candidates[-1]
            remain = target-j
            if remain == 0:
                dp[-1][j].add(tuple())
            if remain == n:
                dp[-1][j].add((n,))
            
        for i in range(len(candidates)-2,-1,-1):
            n = candidates[i]
            for j in range(target+1):
                for t in dp[i+1][j]:
                    dp[i][j].add(t)
                if n+j <= target:
                    for t in dp[i+1][n+j]:
                        tt = tuple(sorted(list(t+(n,))))
                        dp[i][j].add(tt)

        return dp[0][0]

                