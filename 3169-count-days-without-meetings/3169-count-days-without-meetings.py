class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        ans = 0

        meetings.sort()
        
        mx = 0
        for a,b in meetings:
            if a > mx:
                ans += a-mx-1
            mx = max(mx,b)

        if mx < days:
            ans += days-mx
        
        return ans