
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        tree = [0] * (4 * n)
        sq = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def apply(i, s, e, v):
            length = e - s + 1

            sq[i] += 2 * v * tree[i] + v * v * length
            tree[i] += v * length
            lazy[i] += v

            sq[i] %= MOD
            tree[i] %= MOD
            lazy[i] %= MOD

        def push(i, s, e):
            if lazy[i] == 0 or s == e:
                return

            m = (s + e) // 2

            apply(i * 2, s, m, lazy[i])
            apply(i * 2 + 1, m + 1, e, lazy[i])

            lazy[i] = 0

        def update(us, ue, v, i=1, s=0, e=n-1):
            if e < us or ue < s:
                return

            if us <= s and e <= ue:
                apply(i, s, e, v)
                return

            push(i, s, e)

            m = (s + e) // 2

            update(us, ue, v, i*2, s, m)
            update(us, ue, v, i*2+1, m+1, e)

            tree[i] = (tree[i*2] + tree[i*2+1]) % MOD
            sq[i] = (sq[i*2] + sq[i*2+1]) % MOD

        ans = 0
        last = {}

        for i, num in enumerate(nums):
            p = last.get(num, -1)

            update(p + 1, i, 1)

            ans = (ans + sq[1]) % MOD

            last[num] = i

        return ans
