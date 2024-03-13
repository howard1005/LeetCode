class Solution:
    def pivotInteger(self, n: int) -> int:
        tot = (1+n)*n//2
        cum = 0
        for i in range(1,n+1):
            if cum + i == tot - cum:
                return i
            cum += i
        return -1