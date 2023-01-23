class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inds = [0 for _ in range(n+1)]
        outds = [0 for _ in range(n+1)]
        for a,b in trust:
            inds[b] += 1
            outds[a] += 1
        for i in range(n):
            label = i+1
            if inds[label] == n-1 and outds[label] == 0:
                return label
        return -1