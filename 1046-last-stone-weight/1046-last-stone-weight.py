import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        for stone in stones:
            heapq.heappush(h,-stone)
        while len(h)>1:
            stone1,stone2 = -heapq.heappop(h),-heapq.heappop(h)
            diff = abs(stone1-stone2)
            if diff:
                heapq.heappush(h,-diff)
        if h:
            return -h[0]
        else:
            return 0
        