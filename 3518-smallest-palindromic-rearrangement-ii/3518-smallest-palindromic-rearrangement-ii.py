class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        ans = ''
        
        d = defaultdict(int)
        for c in s:
            d[c] += 1

        cl = []
        odd = ''

        for c in d.keys():
            if d[c] % 2 == 0:
                d[c] //= 2
                cl.append(c)
            else:
                odd = c
                d[c] //= 2

        cl.sort()
        if odd:
            cl.append(odd)

        tl = []

        for c in cl:
            tl.extend([c] * d[c])

        cntd = defaultdict(int)

        i = len(tl) - 1
        while i >= 0:
            c = tl[i]
            cntd[c] += 1
            i -= 1
            
        def combination(n, r, limit):
            r = min(r, n - r)
            result = 1

            for i in range(1, r + 1):
                result = result * (n - r + i) // i

                if result >= limit:
                    return limit

            return result

        # cnt에 남아 있는 문자로 만들 수 있는 서로 다른 순열 개수
        def count_permutations(cnt, limit):
            remain = sum(cnt.values())
            result = 1

            for count in cnt.values():
                if count == 0:
                    continue

                # result * 조합값이 limit 이상인지만 확인하면 됨
                required = (limit + result - 1) // result
                value = combination(remain, count, required)

                if value >= required:
                    return limit

                result *= value
                remain -= count

            return result

        # 전체 회문 개수가 k보다 적은 경우
        if count_permutations(cntd, k) < k:
            return ''

        left = []
        chars = sorted(cntd.keys())

        # 회문의 왼쪽 절반을 한 자리씩 결정
        for _ in range(len(tl)):
            for c in chars:
                if cntd[c] == 0:
                    continue

                # 현재 위치에 c를 넣어본다.
                cntd[c] -= 1
                ways = count_permutations(cntd, k)

                if ways >= k:
                    left.append(c)
                    break

                # c로 시작하는 경우들을 건너뛴다.
                k -= ways
                cntd[c] += 1

        left = ''.join(left)
        ans = left + odd + left[::-1]

        return ans