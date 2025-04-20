class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ans = 0

        d = defaultdict(int)
        
        for a in answers:
            d[a] += 1

        for k,v in d.items():
            m = k+1
            cnt = v//m + (1 if v%m else 0)
            ans += cnt*m

        return ans 

        