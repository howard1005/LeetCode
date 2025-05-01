from sortedcontainers import SortedList

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        ans = 0

        tasks.sort(reverse=True)

        def proc(tl):
            # print(tl)
            k = pills
            sl = SortedList()
            for w in workers:
                sl.add(w)

            for t in tl:
                i = sl.bisect_left(t)
                if i < len(sl):
                    sl.pop(i)
                    continue
                elif k:
                    i = sl.bisect_left(t-strength)
                    if i == len(sl):
                        return False
                    if sl[i] < t:
                        k -= 1
                    sl.pop(i)
                else:
                    return False
            
            return True
            

        lo,hi = 1,len(tasks)
        while lo<=hi:
            mi = (lo+hi)//2
            # print(lo,mi,hi)
            if proc(tasks[-mi:]):
                lo = mi+1
                ans = max(ans,mi)
            else:
                hi = mi-1

        return ans