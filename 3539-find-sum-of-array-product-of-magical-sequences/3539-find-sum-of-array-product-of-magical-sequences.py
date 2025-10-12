class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        
        MOD = 1_000_000_007

        def modinv(a, mod=MOD):
            """페르마의 소정리를 이용한 모듈러 역원 계산"""
            return pow(a, mod - 2, mod)

        def precompute_factorials(max_n, mod=MOD):
            fact = [1] * (max_n + 1)
            inv_fact = [1] * (max_n + 1)
            for i in range(2, max_n + 1):
                fact[i] = fact[i - 1] * i % mod
            inv_fact[max_n] = modinv(fact[max_n], mod)
            for i in range(max_n - 1, 0, -1):
                inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod
            return fact, inv_fact

        fact, inv_fact = precompute_factorials(30)
        def nCr_fast(n, r, mod=MOD):
            if r < 0 or r > n:
                return 0
            return fact[n] * inv_fact[r] % mod * inv_fact[n - r] % mod

        @cache
        def dfs(i,m,k,b):
            if i == len(nums):
                if m == 0:
                    if k == b.bit_count():
                        return 1
                return 0

            ret = 0

            for mm in range(m+1):
                # i를 mm개 선택
                bb = b+(1<<i)*mm
                kk = k
                if bb&(1<<i):
                    kk -= 1
                    bb ^= (1<<i)
                if kk < 0:
                    continue
                _ret = dfs(i+1,m-mm,kk,bb)
                if _ret > 0:
                    ret += pow(nums[i],mm,MOD)*nCr_fast(m,mm)*_ret
                    ret %= MOD

            return ret

        ans = dfs(0,m,k,0)

        return ans