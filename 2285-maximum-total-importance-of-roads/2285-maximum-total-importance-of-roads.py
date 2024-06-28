class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        ans = 0
        
        d = defaultdict(int)
        for a,b in roads:
            d[a] += 1
            d[b] += 1

        l = [(v,k) for k,v in d.items()]
        l.sort(reverse=True)

        nn = n
        for cnt,num in l:
            ans += cnt*nn
            nn -= 1
        
        return ans