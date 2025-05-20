class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        l = [0 for _ in range(len(nums))]

        for a,b in queries:
            l[a] += 1
            if b+1<len(l):
                l[b+1] -= 1

        for i in range(1,len(l)):
            l[i] += l[i-1]

        for n,o in zip(nums,l):
            if n > o:
                return False
        
        return True