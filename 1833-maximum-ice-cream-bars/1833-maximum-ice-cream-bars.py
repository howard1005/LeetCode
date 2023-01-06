class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        ans = 0
        
        costs.sort()
        for c in costs:
            if coins - c < 0:
                break
            coins -= c
            ans += 1
            
        return ans