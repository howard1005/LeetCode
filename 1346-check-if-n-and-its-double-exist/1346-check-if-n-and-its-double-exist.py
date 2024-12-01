class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d = defaultdict(list)
        for i,n in enumerate(arr):
            d[n].append(i)
        for n in arr:
            if n == 0:
                if len(d[0]) > 1:
                    return True
            elif 2*n in d:
                return True
        return False