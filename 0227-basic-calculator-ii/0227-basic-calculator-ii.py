class Solution:
     def calculate(self, s: str) -> int:
        st = [0]
        n = 0
        op = ''
        sign = 1
        
        for c in s:
            # print(st)
            if c == ' ':
                pass
            elif c == '+':
                if op == '*':
                    t = st.pop()*n*sign
                    st[-1] += int(t)
                elif op == '/':
                    t = st.pop()/(n*sign)
                    st[-1] += int(t)
                else:
                    st[-1] += n*sign 
                sign = 1
                n = 0
                op = '+'
            elif c == '-':
                if op == '*':
                    t = st.pop()*n*sign
                    st[-1] += t
                elif op == '/':
                    t = st.pop()/(n*sign)
                    st[-1] += int(t)
                else:
                    st[-1] += n*sign 
                sign = -1
                n = 0
                op = '-'
            elif c == '*':
                if op == '*':
                    st[-1] *= n*sign
                elif op == '/':
                    st[-1] = int(st[-1]/(n*sign))
                else:
                    st.append(n*sign)
                sign = 1
                n = 0
                op = '*'
            elif c == '/':
                if op == '*':
                    st[-1] *= n*sign
                elif op == '/':
                    st[-1] = int(st[-1]/(n*sign))
                else:
                    st.append(n*sign)
                sign = 1
                n = 0
                op = '/'
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
        # print(st,n,op,sign)
        if op == '*':
            t = st.pop()*n*sign
            st[-1] += t
        elif op == '/':
            t = st.pop()/(n*sign)
            st[-1] += int(t)
        else:
            st[-1] += n*sign 
        
   
        return st[0]
                
                
            