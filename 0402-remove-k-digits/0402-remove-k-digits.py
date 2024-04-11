class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        idx = -1
        kk = 0
        cnt = 0
        for i,n in enumerate(num):
            if cnt > k:
                break
            if n == '0':
                idx = i
                kk = cnt
            else:
                cnt += 1
        num = num[idx+1:]
        k = k-kk
        if k == 0:
            return num if len(num) else '0'
        
        idx = -1
        st = []
        for i,n in enumerate(num):
            while k and st and st[-1] > n:
                st.pop()
                k -= 1
            if k == 0:
                break
            idx = i
            st.append(n)
        while k and st:
            st.pop()
            k -= 1
        ans = ''.join(st) + num[idx+1:]
        return ans if len(ans) else '0'
    
        
        