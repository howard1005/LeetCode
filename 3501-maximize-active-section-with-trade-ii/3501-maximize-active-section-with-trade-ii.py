from bisect import bisect_left,bisect_right

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        ans = [0 for _ in range(len(queries))]

        cnt = 0
        for c in s:
            if c == '1':
                cnt += 1
        for i in range(len(ans)):
            ans[i] = cnt

        l = []
        coni = 0
        for i in range(len(s)):
            c = s[i]
            if c == '0':
                pass
            else:
                if coni <= i-1:
                    l.append((coni,i-1))
                coni = i+1
        if coni < len(s):
            l.append((coni,len(s)-1))
        # print(l)

        cuml = [0 for _ in range(len(l))]
        for i in range(len(cuml)):
            cuml[i] = l[i][1]-l[i][0]+1
        for i in range(len(cuml)-1):
            cuml[i] += cuml[i+1]
        if cuml:
            cuml[-1] = 0
        # print(cuml)

        x = 0
        while (1<<x) < len(l):
            x += 1
        size = 1<<x
        # print(f"size : {size}")
        
        tree = [0 for _ in range(size*2)]

        def query(us,ue,i=1,s=0,e=size-1):
            if ue < s or e < us:
                return -1
            if us <= s and e <= ue:
                return tree[i]
            
            m = (s+e)//2
            q1 = query(us,ue,i*2,s,m)
            q2 = query(us,ue,i*2+1,m+1,e)

            return max(q1,q2)

        def update(us,ue,uv,i=1,s=0,e=size-1):
            if ue < s or e < us:
                return
            if us <= s and e <= ue:
                tree[i] = uv
                return
            
            m = (s+e)//2
            update(us,ue,uv,i*2,s,m)
            update(us,ue,uv,i*2+1,m+1,e)

            tree[i] = max(tree[i*2],tree[i*2+1])

        for i in range(len(cuml)):
            v = cuml[i]
            update(i,i,v)

        # print(tree)

        for idx,(a,b) in enumerate(queries):
            # [a, b]와 겹치는 첫 번째/마지막 0 구간
            i = bisect_left(l,a,key=lambda x:x[1])
            j = bisect_right(l,b,key=lambda x:x[0])-1

            # 거래하려면 최소 두 개의 0 구간이 필요
            if i >= len(l) or j < 0 or i >= j:
                continue

            qi = i
            qj = j-1
            av = 0
            bv = 0

            # 왼쪽 경계에 걸친 구간
            if l[i][0] < a:
                av = (
                    l[i][1] - a + 1
                    + min(b,l[i+1][1]) - l[i+1][0] + 1
                )
                qi = i+1

            # 오른쪽 경계에 걸친 구간
            if l[j][1] > b:
                bv = (
                    l[j-1][1] - max(a,l[j-1][0]) + 1
                    + b - l[j][0] + 1
                )
                qj = j-2

            q = query(qi,qj) if qi<=qj else 0
            ans[idx] += max(q,av,bv)

            # print(f"query : {a},{b}\n",qi,qj,q,av,bv)


        return ans



        