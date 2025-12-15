class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = 0
        
        j = 0
        for i in range(len(prices)):
            if prices[i-1]-1 != prices[i]:
                j = i
            cnt = i-j+1
            ans += cnt

        return ans