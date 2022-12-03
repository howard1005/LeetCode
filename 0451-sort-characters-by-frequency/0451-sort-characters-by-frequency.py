from collections import defaultdict

class Solution:
    def frequencySort(self, s: str) -> str:
        d = defaultdict(int)
        for c in s:
            d[c] += 1
        l = [(v,k) for k,v in d.items()]
        l.sort()
        l.reverse()
        ans = ''
        for cnt,c in l:
            ans += c*cnt
        return ans