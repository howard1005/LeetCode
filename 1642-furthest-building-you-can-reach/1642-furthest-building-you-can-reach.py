import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        h = []
        cum = 0
        
        for i in range(1,len(heights)):
            diff = heights[i] - heights[i-1]
            if diff > 0:
                heapq.heappush(h, diff)
                if len(h) > ladders:
                    cum += heapq.heappop(h)
            if cum > bricks:
                return i-1
        
        return len(heights)-1
        
                