class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0:
            return -1
        i = 1
        n = 1
        while i < 100000:
            if n % k == 0:
                return i
            n = n%k
            n = n*10 + 1
            i += 1
        return -1