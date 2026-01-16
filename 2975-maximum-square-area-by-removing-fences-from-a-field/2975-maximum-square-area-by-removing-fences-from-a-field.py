class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 1_000_000_007

        hl = [1] + hFences + [m]
        hl.sort()
        hsd = set()
        for i in range(len(hl)):
            for j in range(i+1,len(hl)):
                hsd.add(hl[j]-hl[i])

        vl = [1] + vFences + [n]
        vl.sort()
        vsd = set()
        for i in range(len(vl)):
            for j in range(i+1,len(vl)):
                vsd.add(vl[j]-vl[i])

        # print(hl,vl)
        # print(hsd,vsd)

        sd = hsd & vsd

        if sd:
            le = max(sd)
            return le*le%MOD

        return -1