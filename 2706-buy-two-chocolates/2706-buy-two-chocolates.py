class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        ans = money-(prices[0] + prices[1])
        if ans < 0:
            return money
        return ans
        