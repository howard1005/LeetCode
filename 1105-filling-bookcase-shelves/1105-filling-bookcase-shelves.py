class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        ans = 0

        dp = [inf for _ in range(len(books))]
        dp[-1] = books[-1][1]

        for i in range(len(books)-2,-1,-1):
            x = 0
            y = 0
            j = i
            while j<len(books) and x<shelfWidth:
                w,h = books[j]
                x += w
                y = max(y,h)
                if x <= shelfWidth:
                    dp[i] = min(dp[i],y+(dp[j+1] if j+1<len(books) else 0))
                j += 1
                
        ans = dp[0]

        return ans