class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        ans = 0
        
        def isPrime(n):
            return n in (2,3,5,7,11,13,17,19,23,29,31)

        for n in range(left,right+1):
            cnt = 0
            while n:
                cnt += n&1
                n>>=1
            ans += isPrime(cnt)

        return ans