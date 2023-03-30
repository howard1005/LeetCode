class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        
        d1,d2 = defaultdict(int),defaultdict(int)
        for c1,c2 in zip(s1,s2):
            d1[c1] += 1
            d2[c2] += 1
        if d1 != d2:
            return False
        
        dp = {}
        
        def dfs(s1,s2):
            if len(s1) == 1:
                return True
            
            if (s1,s2) in dp:
                return dp[(s1,s2)]
            dp[(s1,s2)] = False
            
            d1,d2 = defaultdict(int),defaultdict(int)
            for i in range(len(s1)-1):
                c1,c2 = s1[i],s2[i]
                d1[c1] += 1
                d2[c2] += 1
                if d1 == d2:
                    if dfs(s1[:i+1],s2[:i+1]) and dfs(s1[i+1:],s2[i+1:]):
                        dp[(s1,s2)] = True
                        return True
            d1,d2 = defaultdict(int),defaultdict(int)
            for i in range(len(s1)-1):
                c1,c2 = s1[i],s2[-i-1]
                d1[c1] += 1
                d2[c2] += 1
                if d1 == d2:
                    if dfs(s1[:i+1],s2[-i-1:]) and dfs(s1[i+1:],s2[:-i-1]):
                        dp[(s1,s2)] = True
                        return True
            return False
                    
        return dfs(s1,s2)
                    
                