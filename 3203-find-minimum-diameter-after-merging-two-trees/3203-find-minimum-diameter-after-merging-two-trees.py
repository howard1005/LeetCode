class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        
        def proc(edges):
            ret = inf

            d = defaultdict(set)
            for a,b in edges:
                d[a].add(b)
                d[b].add(a)

            pd = defaultdict(dict)

            def down(n,p):
                for nn in d[n]:
                    if nn == p:
                        continue
                    v = down(nn,n)
                    # print(v)
                    pd[n][nn] = v
                l = list(pd[n].values())
                if l:
                    return max(l)+1
                return 1

            print("root : ", edges[0][0])

            down(edges[0][0],-1)

            # print(pd)

            def up(n,p):
                pdd = pd[p]
                mx = 0
                for k,v in pdd.items():
                    if k == n:
                        continue
                    mx = max(mx,v+1)
                pd[n][p] = mx
                    
                for nn in d[n]:
                    if nn == p:
                        continue
                    up(nn,n)

            up(edges[0][0],-1)

            print("pd",pd)
            ret_mx = 0
            for _,pdd in pd.items():
                l = pdd.values()
                if l:
                    mx = max(l)
                    ret_mx = max(ret_mx,mx)
                    ret = min(ret,mx)

            return ret,ret_mx

        ans = 1
        ans_mx = 0
        if edges1:
            mn,mx = proc(edges1)
            ans += mn
            ans_mx = max(ans_mx,mx)
        if edges2:
            mn,mx = proc(edges2)
            ans += mn
            ans_mx = max(ans_mx,mx)

        return max(ans,ans_mx)
            
