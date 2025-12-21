class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0

        n,m = len(strs),len(strs[0])

        l = [i for i in range(n-1)]
        idx = 0

        while l and idx<m:
            # print(l,idx)
            tl = []
            for i in l:
                s1,s2 = strs[i],strs[i+1]
                c1,c2 = s1[idx],s2[idx]
                if c1 < c2:
                    pass
                elif c1 == c2:
                    tl.append(i)
                else:
                    tl = l[:]
                    ans += 1
                    break
            l = tl
            idx += 1

        return ans