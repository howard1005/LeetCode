class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        ans = 0
        
        n = len(colors)
        
        d = defaultdict(lambda: [0 for _ in range(26)])
        # for i,c in enumerate(colors):
        #     d[i][ord(c)-ord('a')] += 1
    
        ind = defaultdict(int)
        ed = defaultdict(list)
        for a,b in edges:
            ed[a].append(b)
            ind[b] += 1
        # print(ed)
        
        vis = {}
        dq = deque()
        for i in range(n):
            if i not in ind:
                vis[i] = 1
                dq.append(i)
        # print(dq)
        
        if not dq:
            return -1
        
        while dq:
            i = dq.popleft()
            d[i][ord(colors[i])-ord('a')] += 1
            ans = max(ans,max(d[i]))
            # print(i,d[i])
            for ni in ed[i]:
                for j in range(26):
                    d[ni][j] = max(d[ni][j],d[i][j])
                ind[ni] -= 1
                if ind[ni] == 0:
                    vis[ni] = 1
                    dq.append(ni)
        
        if len(vis) != n:
            return -1
        
        return ans