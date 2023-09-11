class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans = []
        
        d = defaultdict(list)
        
        for i,g in enumerate(groupSizes):
            if len(d[g]) < g:
                d[g].append(i)
            if len(d[g]) == g:
                ans.append(d[g][:])
                d[g].clear()
                
        return ans