class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        ans = 0

        ed = defaultdict(set)
        for a,b in allowedSwaps:
            ed[a].add(b)
            ed[b].add(a)

        vis = set()
        def bfs(si):
            ret = [si]
            vis.add(si)
            dq = deque([si])
            while dq:
                i = dq.popleft()
                for ni in ed[i]:
                    if ni in vis:
                        continue
                    vis.add(ni)
                    ret.append(ni)
                    dq.append(ni)
            return ret

        for i in range(len(source)):
            if i in vis:
                continue
            l = bfs(i)
            # print(l)
            d1,d2 = defaultdict(int),defaultdict(int)
            for j in l:
                d1[source[j]] += 1
                d2[target[j]] += 1
            # print(d1,d2)
            # print(vis)
            for k in set(d1.keys())|set(d2.keys()):
                ans += abs(d1[k]-d2[k])

        return ans//2