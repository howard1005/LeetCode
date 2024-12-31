class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        def proc(l1,l2):
            ret = 0

            d = defaultdict(int)

            for i in range(len(l1)):
                for j in range(i+1,len(l1)):
                    d[l1[i]*l1[j]] += 1
            
            for n in l2:
                ret += d[n**2]

            return ret

        return proc(nums1,nums2)+proc(nums2,nums1)
            
            