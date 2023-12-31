class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1
        
        d = defaultdict(lambda: [inf,-inf])
        
        for i,c in enumerate(s):
            l = d[c]
            l[0] = min(l[0],i)
            l[1] = max(l[1],i)
        
        for a,b in d.values():
            if a != inf and b != -inf:
                ans = max(ans,b-a-1)
        
        return ans