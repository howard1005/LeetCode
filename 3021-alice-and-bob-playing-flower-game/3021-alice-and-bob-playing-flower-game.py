class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        ans = 0

        on,en = (n+1)//2,n//2
        om,em = (m+1)//2,m//2

        ans = on*em+en*om

        return ans
        