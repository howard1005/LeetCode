class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if len(haystack) < len(needle):
            return -1
    
        d = {}
        
        exp = 27
        mod = 1000000007
        size = len(needle)
        mask = (exp**size)
        e = 0
        for i in range(size):
            n = ord(haystack[i]) - ord('a') + 1
            e = (e*exp + n)%mask
        d[e] = i-size+1
        
        for i in range(size,len(haystack)):
            n = ord(haystack[i]) - ord('a') + 1
            e = (e*exp + n)%mask
            if e not in d:
                d[e] = i-size+1
        
        e = 0
        for i in range(size):
            n = ord(needle[i]) - ord('a') + 1
            e = (e*exp + n)%mask
            
        print(d, e)
        
        if e in d:
            return d[e]
        return -1
        
        
        
        