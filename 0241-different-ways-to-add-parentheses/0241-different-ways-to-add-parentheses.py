class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        ansl = []

        # 1. 사칙연산에서 괄호는 재귀에 해당 즉 괄호 안의 내용은 괄호 없는 세상
        #    괄호가 닫힐때, 모두 처리하면 언제나 괄호가 없는것으로 가정 가능
        # 2. 곱셈, 나눗셈은 그자리에서 처리해도된다
        # 3. 더하기, 뺄셈은 세상이 끝날때 순서대로 처리한다

        def _make_expl(expr):
            retl = []
            n = ''
            for c in expr:
                if c in {'-','+','*'}:
                    retl.append(n)
                    retl.append(c)
                    n = ''
                else:
                    n += c
            retl.append(n)

            return retl
            
        def _eval_from_exprl(exprl,i=0):
            st = []

            while i < len(expr):
                if e == '(':
                    v,i = _eval_from_exprl(exprl,i+1)
                    st.append(v)
                elif e == ')':
                    break
                    
                elif e in {'-','+','*'}:
                    pass
                elif st and st[-1] == '*':
                    pass
                else:
                    st.append(e)
                i += 1
            _eval_group()

            mul_st = []
            for e in st:
                pass
                

            return st[0],i

        exprl = _make_expl(expression)

        # print('exprl : ', exprl)
        

        def dfs(i,j):
            if i == j:
                return [[exprl[i]]]

            l = []
            for k in range(i,j,2):
                e = exprl[k]
                l1 = dfs(i,k)
                l2 = dfs(k+2,j)
                for el1 in l1:
                    for el2 in l2:
                        l.append(['(']+el1+[')']+[exprl[k+1]]+['(']+el2+[')'])

            return l
                    

        l = dfs(0,len(exprl)-1)

        # print(l)
        for el in l:
            expr = ''.join(el)
            # print(expr)
            v = eval(expr)
            # print(v)
            ansl.append(v)

        return ansl

        
                
            
            
        