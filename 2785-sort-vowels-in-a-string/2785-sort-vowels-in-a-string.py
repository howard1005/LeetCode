class Solution:
    def sortVowels(self, s: str) -> str:
        sl = list(s)
        
        d = {'a', 'e', 'i', 'o','u'}
        l = []
        for i,c in enumerate(sl):
            if c.lower() in d:
                l.append((c,i))
                
        l.sort(key=lambda x: ord(x[0]))
        for i,j in enumerate(sorted([t[1] for t in l])):
            sl[j] = l[i][0]
        
        return ''.join(sl)
        