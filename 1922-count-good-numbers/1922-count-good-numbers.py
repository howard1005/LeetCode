class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 1000000007

        ecnt = n//2 + (1 if n&1 else 0)
        ocnt = n//2

        ans = (pow(5,ecnt,MOD)*pow(4,ocnt,MOD))%MOD
        
        return ans