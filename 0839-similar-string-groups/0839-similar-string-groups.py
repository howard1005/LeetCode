class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        ans = 0
        
        def chk(s1,s2):
            l = []
            for c1,c2 in zip(s1,s2):
                if c1 != c2:
                    l.append((c1,c2))
            if not l:
                return True
            if len(l) == 2 and l[0][0] == l[1][1] and l[0][1] == l[1][0]:
                return True
            
        d = defaultdict(list)
        for i in range(len(strs)):
            for j in range(i+1,len(strs)):
                if chk(strs[i],strs[j]):
                    d[i].append(j)
                    d[j].append(i)
        
        vis = {}
        def bfs(i):
            vis[i] = 1
            dq = deque([i])
            while dq:
                n = dq.popleft()
                for nn in d[n]:
                    if nn not in vis:
                        vis[nn] = 1
                        dq.append(nn)
                        
        for i in range(len(strs)):
            if i not in vis:
                ans += 1
                bfs(i)
                
        return ans
        