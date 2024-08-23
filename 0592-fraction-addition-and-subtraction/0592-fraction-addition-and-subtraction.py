class Solution:
    def fractionAddition(self, expression: str) -> str:
        def gcd(a,b):
            a,b = max(a,b),min(a,b)
            while b:
                a,b = b,a%b
            return a

        def lcm(a,b):
            return a*b//gcd(a,b)

        
        l = []
        s = ''
        for c in expression:
            if c in ['+','-']:
                if s:
                    l.append(s)
                s = c
            else:
                s += c
        if s:
            l.append(s)

        # print(l)
        
        ul,dl = [],[]
        for e in l:
            a,b = e.split('/')
            ul.append(int(a))
            dl.append(int(b))

        # print(ul)
        # print(dl)

        dlcm = dl[0]
        for d in dl[1:]:
            dlcm = lcm(dlcm,d)
        
        # print(dlcm)

        cum = 0
        for u,d in zip(ul,dl):
            cum += int(u*(dlcm/d))

        ngcd = abs(gcd(cum,dlcm))

        # print(cum)
        # print(dlcm)
        # print(ngcd)

        


        return f'{cum//ngcd}/{dlcm//ngcd}'
            
            
            
        


        