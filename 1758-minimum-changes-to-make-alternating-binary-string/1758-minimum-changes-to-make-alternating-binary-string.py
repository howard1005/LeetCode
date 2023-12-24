class Solution:
    def minOperations(self, s: str) -> int:
        def proc(m):
            ret = 0
            for i,c in enumerate(s):
                n = int(c)
                if i&1:
                    if n != m:
                        ret += 1
                else:
                    if n != (m^1):
                        ret += 1
            return ret
        
        return min(proc(0),proc(1))