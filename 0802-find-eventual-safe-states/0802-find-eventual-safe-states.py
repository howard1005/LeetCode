class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        ans = []
        
        cnts = []
        dq = deque()
        d = defaultdict(list)
        for i,l in enumerate(graph):
            cnts.append(len(l))
            if cnts[-1] == 0:
                dq.append(i)
            for j in l:
                d[j].append(i)
                
        while dq:
            i = dq.popleft()
            ans.append(i)
            for j in d[i]:
                cnts[j] -= 1
                if cnts[j] == 0:
                    dq.append(j)

        return sorted(ans)