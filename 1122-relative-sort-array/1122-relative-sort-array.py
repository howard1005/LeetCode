class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []

        d = defaultdict(int)
        for n in arr1:
            d[n] += 1
        for n in arr2:
            while d[n]:
                ans.append(n)
                d[n] -= 1
        ends = []
        for k,v in d.items():
            if v:
                ends.extend([k]*v)
        ends.sort()
        ans += ends
            
        return ans