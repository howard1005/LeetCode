class Solution:
    def candy(self, ratings: List[int]) -> int:
        ansl = [1 for _ in range(len(ratings))]
        r = sorted([(v,i) for i,v in enumerate(ratings)])
        for v,i in r:
            if i>0 and ratings[i-1] < v:
                ansl[i] = max(ansl[i],ansl[i-1]+1)
            if i<len(ratings)-1 and ratings[i+1] < v:
                ansl[i] = max(ansl[i],ansl[i+1]+1)
        return sum(ansl)