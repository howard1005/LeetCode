class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        ansl = []

        d = defaultdict(list)
        nodes = set()
        inds = defaultdict(int)
        outds = defaultdict(int)

        def init():
            for a,b in pairs:
                d[a].append(b)
                inds[b] += 1
                outds[a] += 1
                nodes.add(a)
                nodes.add(b)

            s,e = None,None
            
            for n in nodes:
                if inds[n] < outds[n]:
                    s = n
                if  inds[n] > outds[n]:
                    e = n
            
            return s,e
            
        s,e = init()

        if s == None:
            # circuit
            s = e = pairs[0][0]

        vis = set()

        def dfs(i,l):
            for j in d[i]:
                if (i,j) not in vis:
                    vis.add((i,j))
                    dfs(j,l)
            l.append(i)
        
        l = []
        dfs(s,l)

        l.reverse()
        # print(l)

        for i in range(len(l)-1):
            ansl.append((l[i],l[i+1]))

        return ansl