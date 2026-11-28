class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        ans = 0

        items.sort()
        
        n = len(items)

        freq = [0] * (n+1)
        for f, cost in items:
            freq[f] += 1

        d = [0] * (n+1)
        for i in range(1, n+1):
            if freq[i] == 0:
                continue
            for j in range(i, n+1, i):
                d[i] += freq[j]
            d[i] -= 1

        min_cost = min(item[1] for item in items)

        l = [(cost, d[f]) for f, cost in items if d[f] > 0 and cost < min_cost*2]
        l.sort()

        for cost,cnt in l:
            if budget - cost*cnt >= 0:
                budget -= cost*cnt
                ans += cnt*2
            else:
                ans += budget//cost*2
                budget -= budget//cost*cost
                break

        ans += budget//min_cost
        

        return ans