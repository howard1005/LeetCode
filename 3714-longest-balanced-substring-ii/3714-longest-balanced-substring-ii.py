class Solution:
    def longestBalanced(self, s: str) -> int:
        if len(s) == 1:
            return 1
        ans = 0

        hi = 0
        prev = ''
        for i,c in enumerate(s):
            if prev == c:
                ans = max(ans,i-hi+1)
            else:
                prev = c
                hi = i
        
        def two(ex,inc):
            nonlocal ans
            l = [0,0]
            d = {}
            hi = 0
            for i,c in enumerate(s):
                if c == ex:
                    l = [0,0]
                    d = {}
                    hi = i + 1
                    continue
                elif c == inc:
                    l[0] += 1
                else:
                    l[1] += 1
                
                if l[0] and l[0] == l[1]:
                    ans = max(ans,i-hi+1)

                mn = min(l)
                t = (l[0]-mn,l[1]-mn)
                if t[0] == t[1]:
                    ans = max(ans,i-hi+1)
                # print('two',i,l,t,ans)
                if t in d:
                    ans = max(ans,i-d[t])
                else:
                    d[t] = i

        two('a','b')
        two('b','c')
        two('c','a')

        l = [0,0,0]
        d = {}
        for i,c in enumerate(s):
            l[ord(c)-ord('a')] += 1
            mn = min(l)
            t = (l[0]-mn,l[1]-mn,l[2]-mn)
            if t[0] == t[1] and t[1] == t[2]:
                ans = max(ans,i+1)
            # print(i,l,t)
            if t in d:
                ans = max(ans,i-d[t])
            else:
                d[t] = i

            
        return ans