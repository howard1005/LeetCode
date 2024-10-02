class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ansl = [0 for _ in range(len(arr))]

        l = [(v,i) for i,v in enumerate(arr)]
        l.sort()

        r = 0
        for i,(v,j) in enumerate(l):
            if i == 0 or l[i-1][0] != v:
                r += 1
            ansl[j] = r

        return ansl

        