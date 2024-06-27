class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        d = defaultdict(int)
        d[edges[0][0]] += 1
        d[edges[0][1]] += 1
        d[edges[1][0]] += 1
        d[edges[1][1]] += 1
        
        for k,v in d.items():
            if v == 2:
                return k

        return -1
        
        