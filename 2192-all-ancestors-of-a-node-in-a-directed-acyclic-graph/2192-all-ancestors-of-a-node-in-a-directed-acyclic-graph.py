class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans = [set() for _ in range(n)]
        
        d = defaultdict(list)
        ind = defaultdict(int)

        for a,b in edges:
            d[a].append(b)
            ind[b] += 1

        dq = deque([])
        for k in range(n):
            if ind[k] == 0:
                dq.append(k)

        while dq:
            node = dq.popleft()
            for nnode in d[node]:
                ans[nnode] |= ans[node] | {node}
                ind[nnode] -= 1
                if ind[nnode] == 0:
                    dq.append(nnode)

        return ans