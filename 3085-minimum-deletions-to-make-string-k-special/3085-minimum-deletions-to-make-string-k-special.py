class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        ans = inf

        d = defaultdict(int)

        for c in word:
            n = ord(c)-ord('a')
            d[n] += 1
        
        l = list(d.values())

        l.sort()
        
        cum = 0
        for i,a in enumerate(l):
            t = a+k
            _ans = cum
            for j in range(i,len(l)):
                b = l[j]
                if b > t:
                    _ans += b-t
            ans = min(ans,_ans)
            cum += a

        return ans