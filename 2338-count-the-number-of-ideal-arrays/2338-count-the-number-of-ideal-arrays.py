import math

class Solution:
    d = defaultdict(list)
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 1000000007

        ans = 0

        def isPriority(i):
            j = 2
            while j*j<=i:
                if i%j == 0:
                    return False
                j+=1
            return True
        
        d = self.d
        if not d:
            pl = []
            for i in range(2,10001):
                if isPriority(i):
                    pl.append(i)

            for i in range(1,10001):
                m = i
                for p in pl:
                    if m == 1:
                        break
                    cnt = 0
                    while m%p == 0:
                        cnt += 1
                        m//=p
                    d[i].append((p,cnt))

        #최대 숫자m의 인수분해 소수갯수 k일때 (n)^(k)가 n길이의 가짓수

        def nHr(n, r):
            return math.comb(n + r - 1, r)

        for i in range(1,maxValue+1):
            cnt = 1
            for m,r in d[i]:
                cnt *= nHr(n,r)
                cnt %= MOD
            ans += cnt
            ans %= MOD

        return ans
        