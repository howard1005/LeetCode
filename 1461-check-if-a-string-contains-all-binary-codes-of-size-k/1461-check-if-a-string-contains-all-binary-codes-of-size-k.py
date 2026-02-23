class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s)<=k:
            return False
        n = 0
        for i in range(k):
            c = s[i]
            if c == '1':
                n = (n<<1)|1
            else:
                n = (n<<1)
        l = [0 for _ in range(2**k)]
        l[n] = 1
        m = 1<<(k)
        for i in range(1,len(s)-k+1):
            j = i+k-1
            n <<= 1
            if s[j] == '1':
                n |= 1
            n &= ~m
            l[n] = 1
        for v in l:
            if v == 0:
                return False
        return True
            