class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for a in range(1,n):
            b = n-a
            if '0' in str(a) or '0' in str(b):
                continue
            break
            
        return [a,b]
