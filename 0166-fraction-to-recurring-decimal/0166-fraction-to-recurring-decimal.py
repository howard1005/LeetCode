from decimal import Decimal, getcontext

getcontext().prec = 10000  # 유효 자릿수 50자리까지 계산

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'

        ans = ''
        
        def cal_len(b):
            b = abs(b)
            cnt1 = 0
            while b%2 == 0:
                b//=2
                cnt1 += 1
            cnt2 = 0
            while b%5 == 0:
                b//=5
                cnt2 += 1
            # 유한 소수 부분 길이
            fi = max(cnt1,cnt2)

            # 무한 소수 부분 길이
            infi = 0
            if b > 1:
                cnt = 1
                t = 10 % b
                while t != 1:
                    t = (t * 10) % b
                    cnt += 1
                infi = cnt
            
            return fi,infi

        fi,infi = cal_len(denominator)

        if infi == 0:
            m = Decimal(numerator) / Decimal(denominator)
            ans = f"{m:f}"
        else:
            m = Decimal(numerator) / Decimal(denominator)
            s = f"{m:f}"
            l = s.split('.')
            ans = f'{l[0]}.{l[1][:fi]}({l[1][fi:fi+infi]})'
                

        return ans