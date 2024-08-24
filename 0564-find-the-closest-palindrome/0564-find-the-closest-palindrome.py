class Solution:
    def nearestPalindromic(self, n: str) -> str:

        nn = int(n)

        def odd_palindrome(num):
            s = str(num)
            sl = list(s)
            s += ''.join(reversed(sl[:-1]))
            return int(s)

        def even_palindrome(num):
            s = str(num)
            sl = list(s)
            s += ''.join(reversed(sl))
            return int(s)

        def cal(num,palindrome):
            num_palindrome = palindrome(num)
            return (abs(nn-num_palindrome),num_palindrome)

        def proc(palindrome):
            ret = (inf,inf)
            lo,hi = 0,nn
            while lo<=hi:
                mi = (lo+hi)//2
                t = cal(mi,palindrome)
                # print(mi,t)
                if t < ret and t[1] != nn:
                    ret = t
                if t[1] < nn:
                    lo = mi + 1
                elif t[1] > nn:
                    hi = mi - 1
                else:
                    hi = mi - 1
            return ret

        ans = min(proc(odd_palindrome),proc(even_palindrome))

        return str(ans[1])
        

                    
                
                
