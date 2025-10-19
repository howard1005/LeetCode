class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        ans = ''.join(['9' for _ in s])
        
        def get_mod_list(k,n):
            kk = k
            l = [kk%n]
            while 1:
                kk+=k
                m = kk%n
                if m == l[0]:
                    break
                l.append(m)
            return l

        al = get_mod_list(a,10)
        al.sort()
        bl = get_mod_list(b,len(s))
        bl.sort()


        # print(al,bl)

        def rotate(i,l):
            # print('rotate',i,l,l[i:]+l[:-i])
            return l[i:]+l[:i]

        for n in (al if b&1 else [0]):
            sl = [int(c) for c in s]
            for i in range(0,len(s),2):
                sl[i] += n
                sl[i] %= 10
            for m in al:
                sll = sl.copy()
                for j in range(1,len(s),2):
                    sll[j] += m
                    sll[j] %= 10
                # print(n,m,sll)
                for r in bl:
                    rsl = rotate(r,sll)
                    # print('rsl',rsl)
                    ss = ''.join([str(cn) for cn in rsl])
                    # print('ss',ss)
                    ans = min(ans,ss)

            
        return ans