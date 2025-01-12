class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s)&1:
            return False
        
        dq = deque()
        st = []
        for i,(c,lock) in enumerate(zip(s,locked)):
            if lock == '0':
                dq.append(('f',i))
            elif c == ')':
                if st:
                    st.pop()
                else:
                    while dq and dq[0][0]=='o':
                        dq.popleft()
                    if dq:
                        dq.popleft()
                    else:
                        return False
            elif c == '(':
                dq.append(('o',i))
                st.append(i)

        sd = set(st)
        f = 0
        while dq:
            c,i = dq.pop()
            if c == 'f':
                f += 1
            elif c == 'o' and i in sd:
                if f:
                    f -= 1
                else:
                    return False
        
        return True
        
                
                
                        
            
            

                

        