class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        ans = 0

        MOD = 10**9+7

        l = [0 for _ in range(31)]

        for n in nums:
            i = 0
            while n:
                if n&1:
                    l[i] += 1
                i += 1
                n >>= 1

        # print(l)

        bl = [(i,cnt) for i,cnt in enumerate(l)]
        bl.sort(key=lambda x:x[1])

        # print(bl)

        n = (1<<31)-1
        hi = 0
        for i,cnt in bl:
            # print(bin(n),i,cnt)
            if hi < cnt:
                ans += n*n*min(k-hi,(cnt-hi))
                ans %= MOD
                hi = min(k, cnt)
            n ^= (1<<i)
            # print(i,"제거",bin(n))

        return ans

