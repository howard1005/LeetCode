class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        MOD = 1000000007
        BASE = 27

        def nord(c):
            return ord(c)-ord('a')+1

        base_exps = [1]
        for i in range(len(s)):
            base_exps.append((base_exps[-1]*BASE)%MOD)

        
        def cal_exp(n,e):
            if e <= 8:
                return n**e
            _exp = cal_exp(n,e//2)
            # print(_exp)
            return (_exp*_exp*(n if e&1 else 1))%MOD

        def cal_inv(n):
            return cal_exp(n,MOD-2)

        BASE_INV = cal_inv(BASE)
        # print("BASE_INV : ", BASE_INV)
        # print("BASE_INV*BASE : ", (BASE_INV*757)%MOD)

        # print(base_exps)

        def make_odd_pan(i):
            r = s[i+1:]
            l = r[::-1]
            return l+s[i]+r
        
        def make_even_pan(i):
            r = s[i+1:]
            l = r[::-1]
            return l+r

        odd_cands = []
        lh,rh = nord(s[0]),nord(s[0])
        for i in range(1,len(s)):
            c = s[i]

            lh = (lh*BASE + nord(c)) % MOD

            if 2*i >= len(s):
                break

            rh = (rh + base_exps[i]*nord(s[2*i-1]))%MOD
            rh = (rh + base_exps[i+1]*nord(s[2*i]))%MOD
            rh = ((rh - nord(s[i-1]))*BASE_INV)%MOD
            

            # print(lh,rh)

            if lh == rh:
                odd_cands.append(i)


        even_cands = []
        lh,rh = 0,0
        for i in range(len(s)):
            c = s[i]

            lh = (lh*BASE + nord(c)) % MOD

            if 2*i+1 >= len(s):
                break

            rh = (rh + base_exps[i]*nord(s[2*i]))%MOD
            rh = (rh + base_exps[i+1]*nord(s[2*i+1]))%MOD
            rh = ((rh - nord(s[i]))*BASE_INV)%MOD

            if lh == rh:
                even_cands.append(i)

        # print(odd_cands)
        # print(even_cands)


        odd_pan,even_pan = None,None
        if odd_cands:
            odd_pan = make_odd_pan(odd_cands[-1])

        if even_cands:
            even_pan = make_even_pan(even_cands[-1])

        if odd_pan and even_pan:
            if len(odd_pan) < len(even_pan):
                return odd_pan
            return even_pan
        elif odd_pan:
            return odd_pan
        elif even_pan:
            return even_pan
        
        return make_odd_pan(0)
        
        