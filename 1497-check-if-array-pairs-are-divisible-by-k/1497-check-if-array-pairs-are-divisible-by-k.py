class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        d = defaultdict(int)

        for v in arr:
            m = v%k
            t = k-m if m else 0 
            if d[t]:
                d[t] -= 1
            else:
                d[m] += 1

        for k,v in d.items():
            if v:
                return False
        return True
        