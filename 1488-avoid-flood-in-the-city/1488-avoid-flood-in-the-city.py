from heapq import heappush,heappop

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [-1 for _ in range(len(rains))]

        hq = []
        vis = set()
        rd = defaultdict(list)

        for i,r in enumerate(rains[::-1]):
            i = len(rains)-i-1
            rd[r].append((i,r))

        for i,r in enumerate(rains):
            # print(i,r,vis,rd,hq,ans)
            if r == 0:
                if hq:
                    _,rr = heappop(hq)
                    ans[i] = rr
                    vis.remove(rr)
                else:
                    ans[i] = 1
            else:
                if r in vis:
                    return []
                vis.add(r)
                rd[r].pop()
                if rd[r]:
                    ii,rr = rd[r][-1]
                    heappush(hq,(ii,rr))
            # print(i,r,vis,rd,hq,ans)

        return ans