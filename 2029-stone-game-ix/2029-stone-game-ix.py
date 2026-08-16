class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:

        l = [0,0,0]
        for n in stones:
            l[n%3] += 1

        # print(l)

        if l[0]>2:
            l[0] = 2 if l[0]%2==0 else 1

        if l[1]<=l[2]:
            if l[1]>3:
                diff = l[1]-3
                l[1] -= diff
                l[2] -= diff
            if abs(l[1]-l[2])>3:
                l[2] = l[1]+3
        if l[1]>l[2]:
            if l[2]>3:
                diff = l[2]-3
                l[1] -= diff
                l[2] -= diff
            if abs(l[1]-l[2])>3:
                l[1] = l[2]+3

        # print(l)

        def dfs(i, t, r):
            # 돌이 없으면 Bob 승리
            if t[0] == 0 and t[1] == 0 and t[2] == 0:
                return 1

            if r == 0:
                if t[1]:
                    ret = dfs(
                        i ^ 1,
                        (t[0], t[1] - 1, t[2]),
                        (r + 1) % 3
                    )
                    if ret == i:
                        return i

                if t[2]:
                    ret = dfs(
                        i ^ 1,
                        (t[0], t[1], t[2] - 1),
                        (r + 2) % 3
                    )
                    if ret == i:
                        return i

                # 나머지 0인 돌을 고르면 즉시 패배
                return i ^ 1

            if r == 1:
                if t[0]:
                    ret = dfs(
                        i ^ 1,
                        (t[0] - 1, t[1], t[2]),
                        r
                    )
                    if ret == i:
                        return i

                if t[1]:
                    ret = dfs(
                        i ^ 1,
                        (t[0], t[1] - 1, t[2]),
                        (r + 1) % 3
                    )
                    if ret == i:
                        return i

                # 나머지 2인 돌을 고르면 합이 3의 배수가 되어 패배
                return i ^ 1

            if r == 2:
                if t[0]:
                    ret = dfs(
                        i ^ 1,
                        (t[0] - 1, t[1], t[2]),
                        r
                    )
                    if ret == i:
                        return i

                if t[2]:
                    ret = dfs(
                        i ^ 1,
                        (t[0], t[1], t[2] - 1),
                        (r + 2) % 3
                    )
                    if ret == i:
                        return i

                # 나머지 1인 돌을 고르면 합이 3의 배수가 되어 패배
                return i ^ 1

        ret = dfs(0, tuple(l), 0)

        return ret == 0