class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        d = defaultdict(int)
        for i,n in nums1:
            d[i] += n
        for i,n in nums2:
            d[i] += n

        ans = []
        for k,v in d.items():
            ans.append((k,v))
        ans.sort()

        return ans