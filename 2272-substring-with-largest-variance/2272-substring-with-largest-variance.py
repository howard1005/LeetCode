class Solution:
    def largestVariance(self, s: str) -> int:
        ans = 0
        
        sd = list(set(s))
        
        for i in range(len(sd)):
            for j in range(i+1,len(sd)):
                c1,c2 = sd[i],sd[j]
                
                ss = filter(lambda x: x in [c1,c2], s)
                # print(c1,c2)
                
                l = []
                
                c1i,c2i = -1,-1
                
                cum = 0
                for k,c in enumerate(ss):
                    if c == c1:
                        cum += 1
                        c1i = k
                    elif c == c2:
                        cum -= 1
                        c2i = k
                    # print(cum,c1i,c2i,l)
                    
                    if c1i != -1 and c2i != -1:
                        ans = max(ans,abs(cum))
                    
                    if c == c1 and c2i-1 >= 0 and c2i-1 < len(l):
                        mx,mn = l[c2i-1]
                        ans = max(ans,abs(cum-mx),abs(cum-mn))
                    if c == c2 and c1i-1 >= 0 and c1i-1 < len(l):
                        mx,mn = l[c1i-1]
                        ans = max(ans,abs(cum-mx),abs(cum-mn)) 
                    # print(ans)
                        
                    if not l:
                        l.append((cum,cum))
                    else:
                        mx,mn = l[-1]
                        mx,mn = max(mx,cum),min(mn,cum)
                        l.append((mx,mn))

                    
        return ans