from heapq import heappush,heappop
from sortedcontainers import SortedList
class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        ans = []

        od = defaultdict(int)

        freesl = SortedList() # (server_index)
        busyhq = [] # (endtime,server_index)
        for i in range(k):
            freesl.add(i)

        q = deque() # (i,task)
        time = 0
        i = 0
        ti = 0
        while ti < len(arrival):
            a,b = arrival[ti],load[ti]
            ti += 1
            time = a

            while busyhq and busyhq[0][0] <= time:
                et,si = heappop(busyhq)
                freesl.add(si)

            if not freesl:
                continue
            
            fi = freesl.bisect_left((ti - 1) % k)  # 수정
            if fi < len(freesl):
                si = freesl[fi]
            else:
                fi = 0  # 수정: 처음으로 돌아가기
                si = freesl[fi]

            del freesl[fi]
            # 기존 i = (si+1)%k 제거

            
            od[si] += 1

            heappush(busyhq,(a+b,si))

        mx = max(od.values())
        for k,v in od.items():
            if mx == v:
                ans.append(k)

        return ans