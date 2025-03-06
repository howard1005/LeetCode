class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        d = defaultdict(int)

        for r in grid:
            for n in r:
                d[n] += 1

        a,b = None,None
        for n in range(1,len(grid)*len(grid)+1):
            if d[n] == 2:
                a = n
            if d[n] == 0:
                b = n
        
        return a,b
                