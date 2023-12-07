class Solution:
    def largestOddNumber(self, num: str) -> str:
        ans = ""
        
        j = -1
        for i in range(len(num)):
            if int(num[i])&1:
                j = i
        if j != -1:
            ans = num[:j+1]
        
        return ans
        