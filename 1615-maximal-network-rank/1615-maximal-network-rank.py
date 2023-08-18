class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        ans = 0
        
        d = defaultdict(set)
        for a,b in roads:
            d[a].add(b)
            d[b].add(a)
        for a in range(n):
            for b in range(a+1,n):
                ans = max(ans,len(d[a])+len(d[b])-(1 if a in d[b] else 0))
        
        return ans