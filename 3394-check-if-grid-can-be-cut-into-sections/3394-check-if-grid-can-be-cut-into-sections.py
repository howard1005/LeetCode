class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        
        def valid(l):
            cut = 0
            mx = l[0][1]
            for a,b in l[1:]:
                if mx <= a:
                    cut += 1
                    if cut >=2:
                        return True
                mx = max(mx,b)

        l = [(a,c) for a,b,c,d in rectangles]
        l.sort()
        if valid(l):
            return True

        l = [(b,d) for a,b,c,d in rectangles]
        l.sort()
        if valid(l):
            return True

        return False