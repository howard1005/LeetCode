class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        ans = []

        def validc(c):
            if ord('a') <= ord(c) and ord(c) <= ord('z'):
                pass
            elif ord('A') <= ord(c) and ord(c) <= ord('Z'):
                pass
            elif ord('0') <= ord(c) and ord(c) <= ord('9'):
                pass
            elif c == '_':
                pass
            else:
                return False
            return True
        
        def valid(s):
            for c in s:
                if not validc(c):
                    return False
            return True
        
        d = {
            "electronics":0, "grocery":1, "pharmacy":2, "restaurant":3
        }

        l = []

        for s,b,a in zip(code,businessLine,isActive):
            if s and valid(s) and b in d and a:
                l.append((d[b],s))

        l.sort()

        ans = [s for _,s in l]

        return ans
                    
                    
            