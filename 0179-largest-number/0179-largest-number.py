from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        l = [str(n) for n in nums]
        
        def _cmp(a,b):
            if a+b < b+a:
                return 1
            elif a+b > b+a:
                return -1
            return 0

        l.sort(key=cmp_to_key(_cmp))

        ans = ''.join(l)

        return str(int(ans))
            