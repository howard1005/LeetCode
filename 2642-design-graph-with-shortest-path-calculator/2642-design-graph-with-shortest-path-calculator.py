from heapq import heappush,heappop

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.d = defaultdict(list)
        for edge in edges:
            self.addEdge(edge)

    def addEdge(self, edge: List[int]) -> None:
        a,b,c = edge
        self.d[a].append((b,c))

    def shortestPath(self, node1: int, node2: int) -> int:
        d = self.d
        vis = defaultdict(lambda:inf)
        hq = []
        vis[node1] = 0
        heappush(hq,(0,node1))
        while hq:
            c,n = heappop(hq)
            if vis[n] < c:
                continue
            if n == node2:
                return c
            for nn,cc in d[n]:
                if vis[nn] > c + cc:
                    vis[nn] = c + cc
                    heappush(hq,(c + cc,nn))
        return -1
                    
                


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)