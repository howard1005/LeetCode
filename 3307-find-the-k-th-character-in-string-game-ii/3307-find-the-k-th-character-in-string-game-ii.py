class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        
        def dfs(i,a,b):
            # print(i,a,b)
            op = 0
            kk = k
            size = 2**(i+1)

            if a<=k and k<=b:
                pass
            else:
                _k,_op = dfs(i+1,b+1,b+size)
                kk = _k
                op += _op

            ofs = size//2

            if ofs < kk:
                op += operations[i]
                kk -= ofs

            # print(i,a,b,kk,op)
            
            return kk,op

        kk,op = dfs(0,1,1)

        ans = chr((op%26)+ord('a'))

        return ans