class Solution:
    def longestBalanced(self, s: str) -> int:
        ans = 0

        def check(d):
            cnt = None
            for k,v in d.items():
                if v == 0:
                    continue
                if cnt:
                    if cnt != v:
                        return False
                else:
                    cnt = v
            return True
        
        for i in range(len(s)):
            d = defaultdict(int)
            for j in range(i+1):
                d[s[j]] += 1
            
            j = 0
            while j<=i:
                if check(d):
                    ans = max(ans,i-j+1)
                    break
                d[s[j]] -= 1
                j += 1
        
        return ans