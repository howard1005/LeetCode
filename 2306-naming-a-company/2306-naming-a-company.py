class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        ans = 0
        
        vc = set()
        for idea in ideas:
            vc.add(idea[0])
        sd = set(ideas)
        d = defaultdict(int)
        for idea in ideas:
            for c in vc:
                s = c+idea[1:]
                if s not in sd:
                    d[(idea[0],c)] += 1
        for c1 in vc:
            for c2 in vc:
                ans += d[(c1,c2)]*d[(c2,c1)]
                    
        return ans