from sortedcontainers import SortedList

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0

        d = defaultdict(list)
        for i,n in enumerate(nums1):
            d[n].append(i)
        for i,n in enumerate(nums2):
            d[n].append(i)

        l = [(i,j) for _,(i,j) in d.items()]
        l.sort()

        l = [j for _,j in l]

        sl = SortedList()

        cntd = defaultdict(int)

        for i in l:
            cnt = sl.bisect_left(i)
            cntd[i] = cnt
            sl.add(i)

        rsl = SortedList()

        for i in l[::-1]:
            cnt = len(rsl)-rsl.bisect_left(i)
            cntd[i] *= cnt
            rsl.add(i)

        ans = sum(cntd.values())

        return ans