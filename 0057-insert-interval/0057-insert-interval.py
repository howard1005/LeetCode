class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        ans = []
        
        def isOverlap(r1,r2):
            s,e = max(r1[0],r2[0]),min(r1[1],r2[1])
            if s > e:
                return False
            return True
        flag = True
        r2 = newInterval
        for r1 in intervals:
            if isOverlap(r1,r2):
                r2[0],r2[1] = min(r1[0],r2[0]),max(r1[1],r2[1])
            else:
                if flag and r2[1] < r1[0]:
                    ans.append(r2)
                    flag = False
                ans.append(r1)
        if flag:
            if not ans or r2[1] < ans[0][0]:
                ans.insert(0,r2)
            else:
                ans.append(r2)
            
        return ans