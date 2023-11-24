class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        ans = 0
        i,j = 0,len(piles)-2
        while i<j:
            ans += piles[j]
            i+=1
            j-=2
        return ans