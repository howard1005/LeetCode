class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        
        self.d = defaultdict(int)
        
        for n in nums2:
            self.d[n] += 1
        

    def add(self, index: int, val: int) -> None:
        n = self.nums2[index]
        self.d[n] -= 1
        n += val
        self.d[n] += 1
        self.nums2[index] = n
        

    def count(self, tot: int) -> int:
        ret = 0
        for n in self.nums1:
            ret += self.d[tot-n]

        return ret
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)