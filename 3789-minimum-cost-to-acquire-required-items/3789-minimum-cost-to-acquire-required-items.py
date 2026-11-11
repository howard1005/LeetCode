class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        ans = 0

        if costBoth < cost1+cost2:
            mn = min(need1,need2)
            if need1 < need2:
                ans = need1*costBoth + (need2-need1)*min(cost2,costBoth)
            else:
                ans = need2*costBoth + (need1-need2)*min(cost1,costBoth)
        else:
            ans = need1*cost1 + need2*cost2

        return ans