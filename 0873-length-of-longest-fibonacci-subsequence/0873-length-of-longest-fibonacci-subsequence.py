class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        d = defaultdict(int)

        for i in range(len(arr)-1,-1,-1):
            for j in range(i-1,-1,-1):
                a,b = arr[j],arr[i]
                d[(a,b)] = d[(b,a+b)] + 1

        ans = max(d.values())+1

        return ans if ans>2 else 0