class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vs = ('a', 'e', 'i', 'o', 'u')

        d1 = {}
        d2 = {}
        d3 = {}

        def trans(w):

            vl = ['*' if c in vs else c for c in w]
            return ''.join(vl)

        for i,w in enumerate(wordlist):
            if w not in d1:
                d1[w] = i

            lw = w.lower()
            if lw not in d2:
                d2[lw] = i

            vw = trans(lw)
            if vw not in d3:
                d3[vw] = i

        # print(d1)
        # print(d2)
        # print(d3)

        ans = []

        for q in queries:
            lq = q.lower()
            vq = trans(lq)
            if q in d1:
                i = d1[q]
                ans.append(wordlist[i])
            elif lq in d2:
                i = d2[lq]
                ans.append(wordlist[i])
            elif vq in d3:
                i = d3[vq]
                ans.append(wordlist[i])
            else:
                ans.append('')

        return ans
            

            