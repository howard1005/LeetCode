class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        ans = ''

        if t == 1 and '0' not in num:
            return num

        def valid(n):
            d = defaultdict(int)
            for i in (2,3,5,7):
                while n%i == 0:
                    d[i] += 1
                    n //= i
            return n == 1,d

        f,d = valid(t)
        if not f:
            return "-1"

        print(d)

        def make_digits(d):
            l = []

            l.extend([8] * (d[2] // 3))

            if d[2] % 3 == 2:
                l.append(4)
            elif d[2] % 3 == 1:
                l.append(2)

            l.extend([9] * (d[3] // 2))

            if d[3] % 2:
                l.append(3)

            l.extend([5] * d[5])
            l.extend([7] * d[7])

            # 2×3은 6 하나로 합치는 게 더 짧음
            if 2 in l and 3 in l:
                l.remove(2)
                l.remove(3)
                l.append(6)

            # 4×3은 2×6으로 바꾸는 게 사전순으로 더 작음
            elif 4 in l and 3 in l:
                l.remove(4)
                l.remove(3)
                l.extend([2, 6])

            l.sort()
            return l

        l = make_digits(d)

        print(l)
        
        if len(l) > len(num):
            ans = ''.join(str(i) for i in l)
        else:
            factor = {
                1: {},
                2: {2: 1},
                3: {3: 1},
                4: {2: 2},
                5: {5: 1},
                6: {2: 1, 3: 1},
                7: {7: 1},
                8: {2: 3},
                9: {3: 2},
            }

            def subtract(need, digit):
                result = need.copy()

                for p, count in factor[digit].items():
                    result[p] = max(0, result[p] - count)

                return result

            # num의 각 prefix를 사용하고 나서
            # 필요한 소인수가 얼마나 남는지 저장
            prefix = [d.copy()]

            for ch in num:
                digit = int(ch)

                if digit == 0:
                    break

                prefix.append(subtract(prefix[-1], digit))

            # num 자체가 이미 조건을 만족
            if (
                len(prefix) == len(num) + 1
                and all(prefix[-1][p] == 0 for p in (2, 3, 5, 7))
            ):
                return num

            # 오른쪽 자리부터 하나씩 증가시켜 본다.
            start = min(len(num) - 1, len(prefix) - 1)

            for i in range(start, -1, -1):
                current = int(num[i])

                for digit in range(max(1, current + 1), 10):
                    remain = subtract(prefix[i], digit)
                    suffix = make_digits(remain)
                    space = len(num) - i - 1

                    if len(suffix) <= space:
                        ans = (
                            num[:i]
                            + str(digit)
                            + '1' * (space - len(suffix))
                            + ''.join(map(str, suffix))
                        )
                        return ans

            # 같은 길이에서 만들 수 없으면 한 자리 늘린다.
            ans = (
                '1' * (len(num) + 1 - len(l))
                + ''.join(map(str, l))
            )

        return ans

        