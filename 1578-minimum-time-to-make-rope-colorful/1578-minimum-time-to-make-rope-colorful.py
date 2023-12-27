class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        
        cur = ''
        cumCnt = 0
        cumTime = 0
        maxTime = 0
        for c,t in zip(colors,neededTime):
            if cur != c:
                if cumCnt > 1:
                    ans += cumTime - maxTime
                cur = c
                cumCnt = 1
                cumTime = t
                maxTime = t
            else:
                cumCnt += 1
                cumTime += t
                maxTime = max(maxTime,t)
        if cumCnt > 1:
            ans += cumTime - maxTime
            cur = c
            cumCnt = 0
            cumTime = 0
            maxTime = 0
                
        return ans