class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ansd = set()

        def n2d(n):
            retd = defaultdict(int)
            i = 0
            while n:
                if n&1:
                    retd[i]+=1
                i += 1
                n >>= 1
            return retd

        def d2n(d):
            retn = 0
            for i,cnt in d.items():
                if cnt>0:
                    retn |= 1<<i
            return retn

        def subd(d1,d2):
            retd = d1.copy()
            for i in range(32):
                retd[i] -= d2[i]
            return retd

        def addd(d1,d2):
            retd = d1.copy()
            for i in range(32):
                retd[i] += d2[i]
            return retd

        d = defaultdict(int)
        zd = {}

        for n in arr:
            ansd.add(n)
            nd = n2d(n)
            d = addd(d,nd)
            cumn = d2n(d)
            ansd.add(cumn)
            # print(f"n,d : {n},{d}")

            for i,cnt in d.items():
                if cnt:
                    if (i,cnt) in zd:
                        td = zd[(i,cnt)]
                        md = subd(d,td)
                        tn = d2n(md)
                        # print(f"tn : {tn}")
                        ansd.add(tn)
                    else:
                        zd[(i,cnt)] = d

        # print(f"zd : {zd}")
            

        # print(ansd)

        return len(ansd)