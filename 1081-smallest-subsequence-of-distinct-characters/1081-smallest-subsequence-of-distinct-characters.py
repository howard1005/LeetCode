from bisect import bisect_left

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        ans = ''

        last_i = 0
        d = defaultdict(list)
        for i,c in enumerate(s):
            d[c].append(i)
        # print(d)

        cl = list(d.keys())
        cl.sort()

        vis = set()
        last_i = 0
        for idx in range(len(cl)):
            # print(idx,last_i)
            for i in range(len(cl)):
                c1 = cl[i]
                if c1 in vis:
                    continue
                if idx == len(cl)-1:
                    ans += c1
                    break
                idxl = []
                for j in range(len(cl)):
                    c2 = cl[j]
                    if c1 == c2 or c2 in vis:
                        continue
                    idxl.append(d[c2][-1])
                ii = bisect_left(d[c1],last_i)
                j = d[c1][ii]
                if j < min(idxl):
                    ans += c1
                    last_i = j
                    vis.add(c1)
                    break

        return ans