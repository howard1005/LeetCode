class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        ans = ''
        
        outd = defaultdict(int)
        for a,b in paths:
            outd[a] += 1
            outd[b]
        for k,v in outd.items():
            if v == 0:
                ans = k
                
        return ans