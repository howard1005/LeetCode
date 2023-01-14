class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        ans = ''
        
        par = [i for i in range(26)]
        
        def getPar(c):
            i = ord(c) - ord('a')
            tl = []
            while i != par[i]:
                tl.append(i)
                i = par[i]
            for j in tl:
                par[j] = i
            return chr(i + ord('a'))
        
        def merge(c1,c2):
            p1,p2 = getPar(c1),getPar(c2)
            i,j = ord(p1)-ord('a'),ord(p2)-ord('a')
            if i<j:
                par[j] = i
            else:
                par[i] = j
                
        for c1,c2 in zip(s1,s2):
            merge(c1,c2)
        for c in baseStr:
            ans += getPar(c)
                
        return ans