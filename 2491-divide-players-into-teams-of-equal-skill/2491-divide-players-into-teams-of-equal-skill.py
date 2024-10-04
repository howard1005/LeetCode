class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        tot = sum(skill)
        if tot%(len(skill)//2) != 0:
            return -1
        t = tot//(len(skill)//2)

        d = defaultdict(int)

        ans = 0

        for v in skill:
            m = t-v
            if d[m]:
                d[m] -= 1
                ans += v*m
            else:
                d[v] += 1

        for k,v in d.items():
            if v:
                return -1
        
        return ans
                