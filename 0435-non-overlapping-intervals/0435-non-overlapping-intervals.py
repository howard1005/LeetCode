class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        
        intervals.sort()
        
        prev = (-inf,-inf)
        
        for a,b in intervals:
            if a < prev[1]:
                ans += 1
                if b < prev[1]:
                    prev = (a,b)
            else:
                prev = (a,b)
                
        return ans
                