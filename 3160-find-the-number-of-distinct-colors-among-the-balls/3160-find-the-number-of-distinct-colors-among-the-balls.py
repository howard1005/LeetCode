class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ans = []
        
        colors = defaultdict(int)
        d = defaultdict(int)

        for x,y in queries:
            if x in colors:
                c = colors[x]
                d[c] -= 1
                if d[c] == 0:
                    del d[c]
            colors[x] = y
            d[y] += 1
            ans.append(len(d))
                
        return ans