class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        ans = ['1' for _ in range(len(binary))]
        
        a,b = 0,len(binary)-1
        while a < len(binary) and binary[a] == '1':
            a += 1
        while b >= 0 and binary[b] == '1':
            b -= 1
            
        if a >= b:
            return binary
        
        cnt = 0
        for i in range(a,b+1):
            if binary[i] == '1':
                cnt += 1
                
        ans[b-cnt] = '0'        
            
        return ''.join(ans)