class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        
        dp = [[-1 for _ in range(11)] for _ in range(3)]

        sn = str(n)

        # n = 56789이면,
        # 566 상태와 565 상태는 동일한 값을 리턴할것이다.(567보다 작은 모든 숫자에 대해..)
        # 567은 다를 것이다. -> fit만 있으면.. -> [fit][len]
        # 하지만, 600은 566과 같지 않다.
        # fit을 중심으로 1이 fit한거고 큰거는 2 작은거는 0하면 되나? -> 된다

        # input: 숫자 문자열, output: 앞으로 만들 수 있는 숫자 갯수
        def dfs(s):
            if s and int(s) > n:
                return 0

            fit = 0
            if sn[:len(s)] == s:
                fit = 1
            elif sn[:len(s)] < s:
                fit = 2

            if dp[fit][len(s)] != -1:
                return dp[fit][len(s)]

            ret = 1 if s else 0 # 끝내는 경우

            for i in range(10):
                if not s and i == 0:
                    continue
                ret += dfs(s + str(i))
            # print(s,ret)

            dp[fit][len(s)] = ret

            return ret
        # print(dfs(''))
        # print(dfs('1'))
        # print(dfs('11'))

        anss = ''
        
        # s: 만들어진 부분 문자, kk: 순번
        # 123이 만들어졌을때 100이면 123은 101번째 수가 된다(122로 만들수 있는 모든 수가 100개 라는 뜻)
        def proc(s,kk):
            nonlocal anss
            if s and int(s) > n:
                return
            # print("proc", s, kk)
            if kk == k:
                anss = s
                # print("anss", anss)
                return

            cum = 1
            for i in range(10):
                if not s and i == 0:
                    continue
                cnt = dfs(s + str(i))
                if not anss and kk + cum + cnt > k:
                    proc(s+str(i),kk + cum)
                cum += cnt
            
        proc('',0)

        return int(anss) if anss else -1

        
            
                
            