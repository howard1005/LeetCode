class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        
        pcnt = 0
        for r in bank:
            cnt = r.count("1")
            if cnt:
                ans += pcnt*cnt
                pcnt = cnt
        
        return ans