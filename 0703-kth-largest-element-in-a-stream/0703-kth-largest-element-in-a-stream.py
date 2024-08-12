import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.h = []
        if nums:
            nums.sort()
            for n in nums[-min(k,len(nums)):]:
                heapq.heappush(self.h,n)
        
    def add(self, val: int) -> int:
        if len(self.h) < self.k:
            heapq.heappush(self.h,val)
        elif self.h and self.h[0] < val:
            heapq.heappop(self.h)
            heapq.heappush(self.h,val)
        return self.h[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)