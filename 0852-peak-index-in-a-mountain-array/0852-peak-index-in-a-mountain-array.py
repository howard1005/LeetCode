class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:        
        lo,hi = 1,len(arr)-2
        while lo<=hi:
            mi = (lo+hi)//2
            if arr[mi-1] < arr[mi] and arr[mi] > arr[mi+1]:
                return mi
            elif arr[mi-1] < arr[mi]:
                lo = mi+1
            else:
                hi = mi-1
        return -1