class Solution:
    d = defaultdict(list)
    l = []

    def kMirror(self, k: int, n: int) -> int:
        ans = 0

        def num(l):
            ret = 0
            for m in l:
                ret = ret*10+m
            return ret

        def isKPand(dec,k):
            tl = []
            while dec:
                tl.append(dec%k)
                dec //= k
            rtl = list(reversed(tl))
            # print(k,tl,rtl)
            return tl == rtl

        def dfs(i,l,size):
            if i == size//2:
                return
            
            for j in range((1 if i==0 else 0),10):
                l[i] = j

                sl = l[:i+1]
                edec = num(sl+sl[::-1])
                odec = num(sl[:-1]+sl[::-1])

                self.l.append(edec)
                self.l.append(odec)

                # for kk in range(2,10):
                #     if isKPand(edec,kk):
                #         last = self.d[kk][-1] if self.d[kk] else 0
                #         self.d[kk].append(edec)
                #     if isKPand(odec,kk):
                #         last = self.d[kk][-1] if self.d[kk] else 0
                #         self.d[kk].append(odec)

                dfs(i+1,l,size)
        
        if not self.d:
            # print('init')
            size = 12
            dfs(0,[0 for _ in range(size)],size)
            self.l.sort()

            # print(self.d)
            # print(len(self.l))
            # print(self.l[:100] + self.l[-100:])

            for kk in range(2,10):
                for m in self.l:
                    if isKPand(m,kk):
                        self.d[kk].append(m)
                        if len(self.d[kk]) == 30:
                            break
                    
        # for i in range(2,10):
        #     print(f"k: {i}, len: {len(self.d[i])}")

                
        for m in self.d[k][:n]:
            ans += m

        return ans