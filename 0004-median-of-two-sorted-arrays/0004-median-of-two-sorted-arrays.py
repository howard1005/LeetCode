class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # <--edge case 처리
        def simple_ans(nums):
            if len(nums) & 1:
                return nums[len(nums)//2] 
            else:
                return (nums[len(nums)//2]+nums[len(nums)//2-1])/2
        if not nums2:
            return simple_ans(nums1)
        if not nums1:
            return simple_ans(nums2)
        if nums1[-1] <= nums2[0]:
            return simple_ans(nums1+nums2)
        if nums2[-1] <= nums1[0]:
            return simple_ans(nums2+nums1)
        # edge case 처리-->
        
        if len(nums1)<len(nums2):
            nums1,nums2 = nums2,nums1
        
        tot_len = len(nums1)+len(nums2)
        target_m = tot_len//2 + (1 if tot_len&1 else 0)
        print('tot_len : {} target_m : {}'.format(tot_len,target_m))
        lo,hi = 1,len(nums1)
        r = float('inf')
        while lo<=hi:
            m1 = (lo+hi)//2
            m2 = target_m - m1
            mi1,mi2 = m1-1,m2-1
            print(m1,m2)
            if mi2 < 0:
                if r > nums1[mi1]:
                    r = nums1[mi1]
                    i,j = mi1,-1
                hi = m1-1
            elif mi2>=len(nums2):
                #if r > nums2[-1]:
                #    r = nums2[-1]
                #    i,j = -1,len(nums2)-1
                lo = m1+1
            elif nums1[mi1] < nums2[mi2]:
                if r > nums2[mi2]:
                    r = nums2[mi2]
                    i,j = mi1,mi2
                lo = m1+1    
            else:
                if r > nums1[mi1]:
                    r = nums1[mi1]
                    i,j = mi1,mi2
                hi = m1-1
        print(i,j)
        
        tans = None
        if i == -1:
            tans = nums2[j]
        elif j == -1:
            tans = nums1[i]
        else:
            tans = max(nums1[i],nums2[j])
        
        if tot_len & 1:
            return tans
        else:
            t = []
            if i+1<len(nums1) and nums1[i+1]>=tans:
                t.append(nums1[i+1])
            if j+1<len(nums2) and nums2[j+1]>=tans:
                t.append(nums2[j+1])
            if t:
                tans2 = min(t)
                return (tans+tans2)/2
            else:
                return tans
                    
        return 0