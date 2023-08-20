class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        ans = []
        
        gd = defaultdict(list)
        mm = m
        for i,j in enumerate(group):
            if j == -1:
                gd[mm].append(i)
                mm += 1
            else:
                gd[j].append(i)
        
        def tp(l,bl):
            # print("l,bl", l,bl)
            retl = []
            outd = defaultdict(list)
            ind = defaultdict(int)
        
            for i in range(len(bl)):
                for j in bl[i]:
                    outd[j].append(i)
                    ind[i] += 1
                    
            # print(outd,ind)
        
            dq = deque()
            for i in range(len(bl)):
                if ind[i] == 0:
                    dq.append(i)
        
            while dq:
                i = dq.popleft()
                # print(i)
                retl.append(l[i])
                for j in outd[i]:
                    ind[j] -= 1
                    if ind[j] == 0:
                        dq.append(j)
            # print("retl",retl)
            return retl
        
        # print("before gd", gd)
        
                

        for gi in gd:
            l = gd[gi]
            rd = {}
            for i,v in enumerate(l):
                rd[v] = i
            bl = []
            d = set(l)
            for i in l:
                tl = []
                for j in beforeItems[i]:
                    if j in d:
                        tl.append(rd[j])
                bl.append(tl)
            gd[gi] = tp(l,bl)
            if not gd[gi]:
                return []
            
        # print("after gd", gd)
            
        l = [gl for gl in gd.values()]
        rd = {}
        for i,a in enumerate(l):
            for j in a:
                rd[j] = i
        bl = []
        for i,a in enumerate(l):
            sd = set()
            for j in a:
                for k in beforeItems[j]:
                    bi = rd[k]
                    if bi != i:
                        sd.add(bi)   
            bl.append(list(sd))
        ll = tp(l,bl)
        
        # print("ll", ll)
        
        for a in ll:
            ans.extend(a)
            
        if len(ans) != n:
            return []
        return ans