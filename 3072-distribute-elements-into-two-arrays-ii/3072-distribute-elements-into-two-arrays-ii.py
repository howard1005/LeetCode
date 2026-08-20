from sortedcontainers import SortedList

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        al,bl = SortedList(),SortedList()
        al.add(nums[0])
        bl.add(nums[1])
        l1,l2 = [nums[0]],[nums[1]]
        for i in range(2,len(nums)):
            n = nums[i]
            cnt1 = len(al)-al.bisect_right(n)
            cnt2 = len(bl)-bl.bisect_right(n)
            if cnt1 > cnt2:
                al.add(n)
                l1.append(n)
            elif cnt1 < cnt2:
                bl.add(n)
                l2.append(n)
            elif len(al) < len(bl):
                al.add(n)
                l1.append(n)
            elif len(al) > len(bl):
                bl.add(n)
                l2.append(n)
            else:
                al.add(n)
                l1.append(n)

        ans = l1+l2
        
        return ans
        

        