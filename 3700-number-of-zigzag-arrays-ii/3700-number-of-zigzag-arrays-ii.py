class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7

        m = r - l + 1

        if n == 1:

            return m % MOD

        def mat_mul(a, b):

            size = len(a)

            res = [[0] * size for _ in range(size)]

            for i in range(size):

                ri = res[i]

                ai = a[i]

                for k in range(size):

                    if ai[k]:

                        v = ai[k]

                        bk = b[k]

                        for j in range(size):

                            ri[j] = (ri[j] + v * bk[j]) % MOD

            return res

        def mat_vec_mul(mat, vec):

            size = len(vec)

            res = [0] * size

            for i in range(size):

                s = 0

                row = mat[i]

                for j in range(size):

                    s += row[j] * vec[j]

                res[i] = s % MOD

            return res

        def mat_pow_apply(mat, exp, vec):

            while exp:

                if exp & 1:

                    vec = mat_vec_mul(mat, vec)

                mat = mat_mul(mat, mat)

                exp >>= 1

            return vec

        AB = [[0] * m for _ in range(m)]

        BA = [[0] * m for _ in range(m)]

        for i in range(m):

            for j in range(m):

                AB[i][j] = m - max(i, j) - 1

                BA[i][j] = min(i, j)

        steps = n - 1

        q = steps // 2

        up = [1] * m

        down = [1] * m

        up = mat_pow_apply(AB, q, up)

        down = mat_pow_apply(BA, q, down)

        if steps % 2 == 1:

            new_up = [0] * m

            s = 0

            for i in range(m - 1, -1, -1):

                new_up[i] = s

                s = (s + down[i]) % MOD

            new_down = [0] * m

            s = 0

            for i in range(m):

                new_down[i] = s

                s = (s + up[i]) % MOD

            up, down = new_up, new_down

        return (sum(up) + sum(down)) % MOD