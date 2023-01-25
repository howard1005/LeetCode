class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        ans = -1
        
        d = defaultdict(list)
        
        def go(n):
            vis = {}
            dist = 0
            while n != -1 and n not in vis:
                vis[n] = 1
                d[n].append(dist)
                n = edges[n]
                dist += 1
        go(node1),go(node2)
        
        mn = inf
        for i in range(len(edges)):
            l = d[i]
            if len(l) == 2 and mn > max(l):
                mn = max(l)
                ans = i
        
        return ans