class Solution:
    l = []
    def nextBeautifulNumber(self, n: int) -> int:
        ans = 7777777

        def proc(t):
            # print(t)
            l = self.l
            def dfs(d,s):
                if sum(d.values()) == 0:
                    l.append(int(s))
                    return
                for k,v in d.items():
                    if v > 0:
                        d[k] -= 1
                        dfs(d,s+str(k))
                        d[k] += 1
            d = {}
            for v in t:
                d[v] = v
            dfs(d,'')
        

        def dfs1(i,t):
            if i == 10:
                if t and sum(t) <= 7:
                    proc(t) 
                return
            dfs1(i+1,t)
            dfs1(i+1,t+(i,))

        if not self.l:
            # print('inti')
            dfs1(1,tuple())
            self.l.sort()

        # print(len(self.l))

        for v in self.l:
            if v > n:
                return v
        
            
        return ans