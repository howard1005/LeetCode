from heapq import heappush,heappop

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.hq = []
        self.d = {}
        for uid,tid,p in tasks:
            heappush(self.hq,(-p,-tid,uid))
            self.d[tid] = [p,tid,uid]
        

    def add(self, userId: int, taskId: int, priority: int) -> None:
        # print(f"추가: {userId},{taskId},{priority}")
        heappush(self.hq,(-priority,-taskId,userId))
        self.d[taskId] = [priority,taskId,userId]
        

    def edit(self, taskId: int, newPriority: int) -> None:
        self.d[taskId][0] = newPriority
        heappush(self.hq,(-newPriority,-self.d[taskId][1],self.d[taskId][2]))
        

    def rmv(self, taskId: int) -> None:
        # print(f"삭제: {taskId}")
        del self.d[taskId]


    def _valid(self):
        return -self.hq[0][1] not in self.d or -self.hq[0][0] != self.d[-self.hq[0][1]][0] or self.hq[0][2] != self.d[-self.hq[0][1]][2]


    def execTop(self) -> int:
        # print(f"현재 hq,d: {self.hq},{self.d}")
        while self.hq and self._valid():
            heappop(self.hq)
        # print(f"lazy제거후 hq: {self.hq}")

        if not self.hq:
            return -1

        p,tid,uid = heappop(self.hq)
        del self.d[-tid]

        return uid
        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()