class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        def chk(interval1, interval2):
            if interval2[0] <= interval1[0] and interval1[1] <= interval2[1]:
                return True
            return False
        s = set()
        for i in range(len(intervals)):
            for j in range(len(intervals)):
                if i == j: continue
                if chk(intervals[i],intervals[j]):
                    s.add(tuple(intervals[i]))
                    break
        return len(intervals) - len(s)