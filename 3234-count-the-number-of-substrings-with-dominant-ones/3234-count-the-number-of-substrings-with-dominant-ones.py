class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0

        l = [0 for _ in range(len(s))]

        for i,c in enumerate(s):
            if c == '0':
                l[i] = 1
        
        d = {0:-1}
        if l[0] == 1:
            d[1] = 0
        for i in range(1,len(l)):
            l[i] += l[i-1]
            if l[i] not in d:
                d[l[i]] = i
        # print(l)
        # print(d)


        for i in range(len(s)):
            zcnt = l[i]
            for tcnt in range(200):
                if tcnt > zcnt:
                    break
                
                k = i+1-((tcnt+tcnt*tcnt) if tcnt else 1)
                if k < 0:
                    break

                t = zcnt-tcnt
                a,b = -1,i
                if t in d:
                    a = d[t]+1
                if t+1 in d:
                    b = d[t+1]
                # if a > i or b > i:
                #     continue 
                
                if a <= k:
                    ans += min(k,b)-a+1

                # print(i,zcnt,tcnt,k,a,b,ans)
                
                
        
        return ans
        