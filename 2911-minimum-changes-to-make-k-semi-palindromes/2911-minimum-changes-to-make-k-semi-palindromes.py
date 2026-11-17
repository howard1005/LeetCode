class Solution:
    CACHE = [
        tuple(i for i in range(1, n // 2 + 1) if n % i == 0) for n in range(201)
    ]
    def minimumChanges(self, s: str, k: int) -> int:

        def get_proper_divisors(n: int) -> tuple[int, ...]:
            return self.CACHE[n]
        
        def min_changes_to_palindrome(s: str) -> int:
            count = 0
            n = len(s)
            
            for i in range(n // 2):
                if s[i] != s[n - 1 - i]:
                    count += 1
                    
            return count

        @cache
        def min_semi_palindrome(s):
            t = get_proper_divisors(len(s))
            ret = inf

            for d in t:
                cnt = 0
                for r in range(d):
                    cnt += min_changes_to_palindrome(s[r::d])
                ret = min(ret, cnt)

            return ret

        @cache
        def dfs(i, k):
            if i >= len(s):
                if k:
                    return inf
                return 0

            if k == 0:  # 추가
                return inf

            ret = inf

            for j in range(i+1, len(s)):
                ts = s[i:j+1]
                ret = min(
                    ret,
                    min_semi_palindrome(ts) + dfs(j+1, k-1)
                )

            return ret

        ans = dfs(0,k)

        return ans
                
            

            