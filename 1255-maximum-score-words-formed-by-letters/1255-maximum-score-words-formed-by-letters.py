class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        n = len(words)
        dp = [-1 for _ in range(1<<n)]

        d = defaultdict(int)
        for c in letters:
            d[c] += 1

        fd = defaultdict(lambda:defaultdict(int))
        for i,w in enumerate(words):
            for c in w:
                fd[i][c] += 1

        def validWord(i):
            for c,cnt in fd[i].items():
                if d[c] < cnt:
                    return False
            return True

        def useWord(i):
            ret = 0
            for c,cnt in fd[i].items():
                d[c] -= cnt
                ret += cnt*score[ord(c)-ord('a')]
            return ret
        
        def unUseWord(i):
            for c,cnt in fd[i].items():
                d[c] += cnt

        def dfs(sta):
            if sta == (1<<n)-1:
                return 0
            if dp[sta] != -1:
                return dp[sta]
            dp[sta] = 0

            for i in range(n):
                if sta & (1<<i) == 0:
                    if validWord(i):
                        gain = useWord(i)
                        dp[sta] = max(dp[sta], dfs(sta|(1<<i)) + gain) 
                        unUseWord(i)
            
            return dp[sta]

        ans = dfs(0)

        return ans
        
            