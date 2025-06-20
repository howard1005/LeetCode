class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        ans = 0

        vl,hl = [0,0],[0,0]
        for c in s:
            if c == 'N':
                vl[0] += 1
            if c == 'S':
                vl[1] += 1
            if c == 'E':
                hl[0] += 1
            if c == 'W':
                hl[1] += 1
            
            t = max(vl)+max(hl)

            v,h = min(vl),min(hl)

            if v+h <= k:
                ans = max(ans,t+v+h)
            else:
                ans = max(ans,t+k-(v+h-k))


        return ans