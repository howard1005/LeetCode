class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        ans = 0

        d = defaultdict(int)
        
        for a,b in dominoes:
            t = (min(a,b),max(a,b))
            d[t] += 1

        for _,v in d.items():
            ans += v*(v-1)//2

        return ans