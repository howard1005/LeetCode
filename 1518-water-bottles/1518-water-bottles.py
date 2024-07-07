class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        
        b,e = numBottles,0
        while b:
            ans += b
            e += b
            b,e = e//numExchange,e%numExchange
            
        return ans    