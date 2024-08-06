class Solution:
    def minimumPushes(self, word: str) -> int:
        ans = 0
        
        d = defaultdict(int)
        for c in word:
            d[c] += 1

        l = [(v,k) for k,v in d.items()]
        l.sort(key=lambda x: -x[0])
        print(l)

        sp = 0
        for cnt,n in l:
            ans += (sp//8+1)*cnt
            sp += 1

        return ans