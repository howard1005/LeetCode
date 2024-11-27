class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:

        d = defaultdict(list)

        for i in range(n-1):
            d[i].append(i+1)
            # d[i+1].append(i)

        def bfs():
            vis = set([0])
            dq = deque([(0,0)])

            while dq:
                i,c = dq.popleft()
                # print(i,c)
                if i == n-1:
                    return c
                for j in d[i]:
                    if j in vis:
                        continue
                    vis.add(j)
                    dq.append((j,c+1))

            return inf

        ansl = []

        for a,b in queries:
            d[a].append(b)
            # d[b].append(a)
            # print("\n\nquri : ", a,b)
            ansl.append(bfs())

        return ansl
        

            