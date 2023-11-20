class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        ans = 0
        
        d = defaultdict(int)
        for i,s in enumerate(garbage):
            for c in s:
                d[c] = i
                ans += 1
        cum = 0
        for i,t in enumerate(travel):
            cum += t
            for v in d.values():
                if i+1==v:
                    ans += cum
                
        return ans