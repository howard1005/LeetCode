class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        
        d = defaultdict(list)
        for i,c in enumerate(s):
            d[c].append(i)
        l = [(l[0],l[-1]) for c,l in d.items()]
        l.sort()

        s,e = 0,0
        for a,b in l:
            if e<a:
                ans.append(e-s+1)
                s = a
            e = max(e,b)
        ans.append(e-s+1)

        return ans