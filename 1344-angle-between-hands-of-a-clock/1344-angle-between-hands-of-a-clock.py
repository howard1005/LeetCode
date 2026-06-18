class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hunit = 30.0
        munit = 6.0
        
        hdeg = (hour%12)*hunit+(minutes/60*hunit)
        mdeg = (minutes%60)*munit
        
        diff = abs(hdeg-mdeg)
       
        return min(diff,360.0-diff)