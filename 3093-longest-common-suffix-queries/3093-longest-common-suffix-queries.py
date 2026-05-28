class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        ans = [-1 for _ in range(len(wordsQuery))]

        MOD = 999999999998631839

        mnle = inf
        mni = inf

        d = defaultdict(list)
        for i,w in enumerate(wordsContainer):
            if len(w) < mnle:
                mnle = len(w)
                mni = i
            h = 0
            exp = 0
            for j in range(len(w)-1,-1,-1):
                c = w[j]
                h = (ord(c)-ord('a')+1)*pow(27,exp,MOD) + h
                h %= MOD
                d[h].append((len(w),i))
                exp += 1
        
        for _,l in d.items():
            l.sort()

        # print(d)

        for i,w in enumerate(wordsQuery):
            h = 0
            exp = 0
            ansi = inf
            for j in range(len(w)-1,-1,-1):
                c = w[j]
                h = (ord(c)-ord('a')+1)*pow(27,exp,MOD) + h
                h %= MOD
                if d[h]:
                    # print('hit',i,w,h)
                    _,idx = d[h][0]
                    ansi = idx
                exp += 1
            ans[i] = ansi if ansi != inf else mni

        return ans