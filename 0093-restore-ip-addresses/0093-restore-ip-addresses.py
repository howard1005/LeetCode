from itertools import combinations

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4 or 12 < len(s):
            return []
        
        ans = []
        
        def validN(s):
            if len(s) > 1 and s[0] =='0':
                return False
            if 255 < int(s):
                return False
            return True
        
        def validIp(l):
            for n in l:
                if validN(n) == False:
                    return False
            return True
        
        l = list(combinations(range(len(s)-1), 3))        
        for a,b,c in l:
            ipl = [
                s[:a+1],
                s[a+1:b+1],
                s[b+1:c+1],
                s[c+1:]
            ]
            if validIp(ipl):
                ans.append('.'.join(ipl))

        return ans