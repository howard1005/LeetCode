class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles

        f,e = 0,numBottles

        while f+e >= numExchange:
            while e >= numExchange:
                e -= numExchange
                f += 1
                numExchange += 1
            ans += f
            e += f
            f = 0
        
        return ans