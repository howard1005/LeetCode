class Solution:
    d = {}
    def sortByBits(self, arr: List[int]) -> List[int]:
        d = self.d
        if not d:
            for i in range(10001):
                cnt = 0
                n = i
                while n:
                    cnt += (n&1)
                    n >>= 1
                d[i] = cnt
        
        arr.sort(key=lambda x:(d[x],x))
        
        return arr