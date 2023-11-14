class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ansl = set()
        
        d = defaultdict(list)
        for i in range(len(s)):
            c = s[i]
            if c not in d:
                d[c].append(i)
        for i in range(len(s)-1,-1,-1):
            c = s[i]
            if len(d[c]) == 1:
                d[c].append(i)
        
        for i,c in enumerate(s):
            for k,l in d.items():
                if len(l) == 2:
                    a,b = l
                    if a < i and i < b:
                        ansl.add((k,c,k))
            
        return len(ansl)