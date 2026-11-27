class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        ans = 0

        items.sort()
        
        d = defaultdict(int)

        for i in range(len(items)):
            d[i] = 1
            for j in range(len(items)):
                if i == j:
                    continue
                if items[j][0]%items[i][0] == 0:
                    d[i] += 1

        dp = [0] * (budget + 1)

        for i, cnt in d.items():
            cost = items[i][1]

            for b in range(budget, cost - 1, -1):
                dp[b] = max(dp[b], dp[b-cost] + cnt)

        min_cost = min(item[1] for item in items)

        for b in range(budget + 1):
            ans = max(ans, dp[b] + (budget-b)//min_cost)

        return ans