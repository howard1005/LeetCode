from heapq import heappush,heappop

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        ans = [-1 for _ in range(len(tasks))]

        freehq = [] # (weight,server_index)
        busyhq = [] # (endtime,server_index)
        for i,s in enumerate(servers):
            heappush(freehq,(s,i))

        q = deque() # (i,task)
        time = 0
        ti = 0
        while 1:
            while busyhq and busyhq[0][0] <= time:
                et,si = heappop(busyhq)
                heappush(freehq,(servers[si],si))

            while ti < len(tasks) and ti < time:
                q.append((ti,tasks[ti]))
                ti += 1

            while q and freehq:
                i,task = q.popleft()
                sw,si = heappop(freehq)
                heappush(busyhq,(time+task,si))
                ans[i] = si

            if freehq and ti < len(tasks):
                time += 1
            else:
                if busyhq:
                    time = busyhq[0][0]
                else:
                    break

        return ans