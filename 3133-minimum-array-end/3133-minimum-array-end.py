class Solution:
    def minEnd(self, n: int, x: int) -> int:
        ans = x

        y = n-1

        j = 0
        for i in range(32):
            k = (y>>i)&1
            while (x>>j)&1:
                j += 1
            # print(i,j,k)
            ans |= k<<j
            j += 1
        
        return ans