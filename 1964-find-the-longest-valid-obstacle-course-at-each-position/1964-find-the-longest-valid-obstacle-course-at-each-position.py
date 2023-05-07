from bisect import bisect_right

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        ans = []
        
        l = []
        
        for o in obstacles:
            i = bisect_right(l,o)
            ans.append(i+1)
            if len(l) == i:
                l.append(o)
            else:
                l[i] = o
        
        return ans