class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def proc(tar):
            c,bc,tc = 0,0,0
            for i in range(len(tops)):
                if tops[i] == tar or bottoms[i] == tar:
                    c += 1
                if tops[i] == tar:
                    tc += 1
                if bottoms[i] == tar:
                    bc += 1
            if c == len(tops):
                return len(tops) - max(bc,tc)
            return float('inf')
        ans = min(proc(tops[0]),proc(bottoms[0]))
        if ans == float('inf'):
            return -1
        return ans
        

            
            