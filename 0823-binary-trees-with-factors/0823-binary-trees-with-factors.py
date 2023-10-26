class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        d = {n:i for i,n in enumerate(arr)}
        l = [1 for _ in range(len(arr))]
        for i in range(len(l)):
            for j in range(i+1):
                n = arr[i] * arr[j]
                if i == j:
                    if n in d:
                        l[d[n]] += l[i] * l[j]
                        l[d[n]] %= 1000000007
                else:
                    if n in d:
                        l[d[n]] += l[i] * l[j] * 2
                        l[d[n]] %= 1000000007
        return sum(l) % 1000000007