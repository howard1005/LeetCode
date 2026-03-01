class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(list(n),key=lambda x:int(x)))