class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ""
        
        t = -1
        for i in range(len(num)-2):
            if num[i] == num[i+1] and num[i+1] == num[i+2]:
                t = max(t,int(num[i:i+3]))
        if t != -1:
            if t == 0:
                ans = "000"
            else:
                ans = str(t)
        
        return ans