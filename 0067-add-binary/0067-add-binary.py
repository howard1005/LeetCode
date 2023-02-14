class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def dec(s):
            n = 0
            for c in s:
                n <<= 1
                if c == '1':
                     n += 1
            return n
        def enc(n):
            if n == 0:
                return '0'
            s = ''
            while n:
                s = str(n%2) + s
                n >>= 1
            return s
        
        return enc(dec(a)+dec(b))