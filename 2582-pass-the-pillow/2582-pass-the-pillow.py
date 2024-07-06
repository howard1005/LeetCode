class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        k,m = time//(n-1),time%(n-1)
        return n-m if k&1 else 1+m