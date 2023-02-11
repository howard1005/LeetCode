class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        ans = [-1 for _ in range(n)]
        
        d = defaultdict(list)
        for a,b in redEdges:
            d[(a,0)].append(b)
        for a,b in blueEdges:
            d[(a,1)].append(b)
        
        vis = {}
        dq = deque([(0,0,0),(0,1,0)])
        while dq:
            node,color,dist = dq.popleft()
            if ans[node] == -1:
                ans[node] = dist
            nextColor = (color ^ 1)
            for nextNode in d[(node,nextColor)]:
                if (nextNode,nextColor) not in vis:
                    vis[(nextNode,nextColor)] = 1
                    dq.append((nextNode,nextColor,dist+1))
        
        return ans