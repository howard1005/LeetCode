from collections import defaultdict

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mn = float('inf')
        d = defaultdict(list)
        for i in range(len(arr)-1):
            d[abs(arr[i]-arr[i+1])].append([arr[i],arr[i+1]])
            mn = min(mn,abs(arr[i]-arr[i+1]))
        return d[mn]