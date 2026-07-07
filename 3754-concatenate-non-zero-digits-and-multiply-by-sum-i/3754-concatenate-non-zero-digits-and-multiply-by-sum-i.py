class Solution:
    def sumAndMultiply(self, n: int) -> int:
        ans = 0

        l = [c for c in list(str(n)) if c != '0']
        
        if not l:
            return 0
        
        ans = int(''.join(l))*sum([int(c) for c in l])

        return ans