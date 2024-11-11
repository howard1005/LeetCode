from bisect import bisect_left

class Solution:
    prl = list()
    def primeSubOperation(self, nums: List[int]) -> bool:
        ans = True

        def _isPrime(n):
            i = 2
            while i*i <= n:
                if n%i == 0:
                    return False
                i += 1
            return True

        def _init():
            prl = self.prl
            if not prl:
                for n in range(2,1001):
                    if _isPrime(n):
                        prl.append(n)
            return prl    
        
        prl = _init()

        prev = nums[-1]
        for n in nums[::-1][1:]:
            if prev <= n:
                diff = n - prev
                i = bisect_left(prl,diff+1)
                if i == len(prl) or n <= prl[i]:
                    return False
                prev = n-prl[i]
            else:
                prev = n

        return ans

