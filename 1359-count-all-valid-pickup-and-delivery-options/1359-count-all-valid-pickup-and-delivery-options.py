class Solution:
    ans = []
    def countOrders(self, n: int) -> int:
        if len(self.ans) == 0:
            self.ans.append(1)
            for i in range(1,501):
                self.ans.append(self.ans[-1]*i*(2*i-1)%1000000007)
        return self.ans[n]