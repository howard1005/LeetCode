class Solution:
    def maximumLength(self, s: str) -> int:
        ans = 0

        d = defaultdict(int)

        prev = ''
        cnt = 0
        for size in range(1,len(s)+1):
            for i in range(len(s)-size+1):
                ss = s[i:i+size]
                d[ss] += 1

        for k,v in d.items():
            if v >= 3:
                ans = max(ans,len(k))

        return ans if ans > 0 else -1