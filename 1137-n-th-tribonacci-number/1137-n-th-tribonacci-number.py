class Solution:
    def tribonacci(self, n: int) -> int:
        tl = [0,1,1]
        for i in range(3,n+1):
            tl.append(tl[i-1]+tl[i-2]+tl[i-3])
        return tl[n]