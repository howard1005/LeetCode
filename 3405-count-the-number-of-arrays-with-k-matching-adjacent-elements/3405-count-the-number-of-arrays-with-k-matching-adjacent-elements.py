from math import comb

class Solution:
    fact = []
    inv_fact = []

    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        MOD = 1_000_000_007
        MAX = 10**5  # n의 최대값에 맞춰 설정

        if not self.fact:
            # 미리 팩토리얼과 역팩토리얼을 계산
            self.fact.extend([1] * (MAX + 1))
            self.inv_fact.extend([1] * (MAX + 1))

            fact = self.fact
            inv_fact = self.inv_fact

            # 팩토리얼
            for i in range(1, MAX + 1):
                fact[i] = fact[i - 1] * i % MOD

            # 역팩토리얼 (페르마의 소정리 이용)
            inv_fact[MAX] = pow(fact[MAX], MOD - 2, MOD)
            for i in range(MAX, 0, -1):
                inv_fact[i - 1] = inv_fact[i] * i % MOD

        fact = self.fact
        inv_fact = self.inv_fact

        # 조합 함수
        def nCr(n, r):
            if r < 0 or r > n:
                return 0
            return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD

        ans = (nCr(n-1,k)*m*pow(m-1,n-k-1,MOD))%MOD

        return ans