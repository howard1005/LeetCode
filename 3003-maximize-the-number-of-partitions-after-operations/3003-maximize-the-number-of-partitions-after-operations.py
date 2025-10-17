class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        ans = 0

        cuml = [[0]*26 for _ in range(len(s))]

        def c2n(c):
            return ord(c)-ord('a')

        def count(l):
            cnt = 0
            for v in l:
                if v>0:
                    cnt += 1
            return cnt

        for i,c in enumerate(s):
            if i >= 1:
                cuml[i] = cuml[i-1].copy()
            cuml[i][c2n(c)] += 1

        # print(cuml)
        
        @cache
        def cal(a,b):
            retl = []
            cnt = 0
            if a > 0:
                for v1,v2 in zip(cuml[b],cuml[a-1]):
                    retl.append(v1-v2)
                    if retl[-1]>0:
                        cnt += 1
            else:
                for v in cuml[b]:
                    retl.append(v)
                    if retl[-1]>0:
                        cnt += 1
            return retl,cnt

        pref = [-1 for _ in range(len(s))]
        suff = [-1 for _ in range(len(s))]
        partition_start = [-1 for _ in range(len(s))]

        sd = set()
        start = 0
        idx = 0
        for i in range(len(s)):
            c = s[i]
            if c not in sd:
                if len(sd) == k:
                    idx += 1
                    sd = set()
                    start = i
            sd.add(c)
            pref[i] = idx+1
            partition_start[i] = start

        def findr(start,i,c,cc):
            r = -1
            lo,hi = start,len(s)-1
            while lo<=hi:
                mi = (lo+hi)//2
                l,cnt = cal(start,mi)
                # print(cnt)
                if c != cc and i<=mi:
                    if l[c2n(c)] == 1:
                        cnt -= 1
                    if l[c2n(cc)] == 0:
                        cnt += 1
                if cnt <= k:
                    lo = mi+1
                    r = max(r,mi)
                else:
                    hi = mi-1
            # print("findr",start,i,c,cc,r)
            return r

        @cache
        def tail(i):
            if i == len(s):
                return 0
            ret = 1
            c = s[i]
            r = findr(i,i,c,c)
            ret += tail(r+1)
            return ret

        for i in range(len(s)):
            suff[i] = tail(i)

        # print(pref,suff,partition_start)



        for i in range(len(s)):
            c = s[i]
            for ofs in range(26):
                _ans = 0
                cc = chr(ord('a')+ofs)
                if c == cc:
                    continue
                start = partition_start[i]
                _ans += pref[start-1] if start else 0

                r = findr(start,i,c,cc)
                # print("r",i,c,cc,r)
                if r>=i:
                    _ans += 1 + (suff[r+1] if r+1<len(suff) else 0)
                else:
                    r2 = findr(i,i,c,cc)
                    # print("r2",i,c,cc,r2)
                    _ans += 2 + (suff[r2+1] if r2+1<len(suff) else 0)

                ans = max(ans,_ans)
                    
        return ans