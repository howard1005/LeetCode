class Solution:
    def minimumLength(self, s: str) -> int:
        ans = len(s)
        
        l = []
        cnt = 0
        prev = ''
        for c in s:
            if c == prev:
                cnt += 1
            else:
                if prev:
                    l.append((prev,cnt))
                cnt = 1
                prev = c
        l.append((prev,cnt))
    
                
        i,j = 0,len(l)-1
        while i<j:
            if l[i][0] == l[j][0]:
                ans -= l[i][1]+l[j][1]
            else:
                break
            i+=1
            j-=1
        if i == j and l[i][1] > 1:
            ans = 0
        
        
        return ans