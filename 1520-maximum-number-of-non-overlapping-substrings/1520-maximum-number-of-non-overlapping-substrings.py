class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        ans = []

        d = defaultdict(lambda:[-1,-1])
        for i,c in enumerate(s):
            if d[c][0] == -1:
                d[c][0] = i
                d[c][1] = i
            else:
                d[c][1] = i

        # print(d)

        def inter(a,b,i,j):
            if a < i and i < b:
                return True
            if a < j and j < b:
                return True
            return False

        l = []
        for nc in range(26):
            c = chr(ord('a')+nc)
            if c not in d:
                continue

            a,b = d[c]
            sd = set([c])

            # 여기만 수정
            k = a
            ok = True
            while k <= b:
                tc = s[k]
                i,j = d[tc]

                # tc가 현재 substring보다 앞에서 이미 등장했다면
                # a부터 시작하는 substring은 불가능
                if i < a:
                    ok = False
                    break

                sd.add(tc)
                b = max(b,j)

                k += 1

            if ok:
                l.append([a,b,sd])

        # print(l)

        # 끝나는 위치가 빠른 순서
        # 같은 b면 더 짧은 구간(큰 a)을 먼저
        l.sort(key=lambda x: (x[1], -x[0]))

        last = -1
        for i in range(len(l)):
            a,b,sd = l[i]

            if a > last:
                ans.append(s[a:b+1])
                last = b
            
            
                


        return ans