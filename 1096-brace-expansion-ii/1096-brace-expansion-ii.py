class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        ans = []


        def dfs(i):
            ret = set()
            sd = set()

            def proc(t):
                nonlocal sd
                tsd = set()
                if isinstance(t,set):
                    if not sd:
                        tsd |= t
                    else:
                        for a in sd:
                            for b in t:
                                tsd.add(a+b)
                else:
                    if not sd:
                        tsd.add(t)
                    else:
                        for a in sd:
                            tsd.add(a+t)
                sd = tsd
                    
                

            while 1:
                if i >= len(expression):
                    ret |= sd
                    return ret,i
                c = expression[i]
                if c == '{':
                    t,i = dfs(i+1)
                    proc(t)
                elif c == '}':
                    ret |= sd
                    return ret,i
                elif c == ',':
                    ret |= sd
                    sd = set()
                else:
                    proc(c)

                i += 1
                    

        sd,_ = dfs(0)
        #print(sd)
        ans = sorted(list(sd))
            

        return ans