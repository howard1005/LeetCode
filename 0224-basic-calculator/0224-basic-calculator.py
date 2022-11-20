class Solution:
    def calculate(self, s: str) -> int:
        st = [0]
        n = 0
        sign = 1
        
        for c in s:
            # print(st)
            if c == ' ':
                pass
            elif c == '+':
                st[-1] += n*sign 
                sign = 1
                n = 0
            elif c == '-':
                st[-1] += n*sign 
                sign = -1
                n = 0
            elif c == '(':
                st.extend([sign,0])
                sign = 1
            elif c == ')':
                t = (st.pop()+n*sign)*st.pop()
                st[-1] += t
                sign = 1
                n = 0
            else:
                n = n*10 + int(c)
        st[-1] += n*sign 
        # print(st)
        
   
        return st[0]
                
                
            
            