class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        ans = ''
        
        l = []
        t = ['']
        for c in s:
            if c.isdigit():
                t.append(int(c))
                l.append(tuple(t))
                t = ['']
            else:
                t[0] += c
                
        if not l:
            return s[k-1]
        
        cuml = [len(l[0][0])*l[0][1]]
        for i in range(1,len(l)):
            cuml.append((cuml[-1]+len(l[i][0]))*l[i][1])
        
        # print(l,cuml)
        
        
        i = -1
        for j in range(len(cuml)):
            if cuml[j] >= k:
                i = j
                break
        
        kk = k
        while i>=0:
            # print(i,kk)
            ofs = 0 if i == 0 else cuml[i-1]
            a = len(l[i][0])
            c = 0
            for _ in range(l[i][1]):
                if c + ofs < kk and kk <= c + ofs + a:
                    return l[i][0][kk - c - ofs-1]
                if kk <= c + ofs + a:
                    break
                
                c += ofs + a
            kk = kk - c
            i = i-1
        
        
        
        return ans