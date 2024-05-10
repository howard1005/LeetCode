from heapq import heappush,heappop

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        l = []
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                l.append((arr[i]/arr[j],(arr[i],arr[j])))
        l.sort()
        return l[k-1][1]
            

        