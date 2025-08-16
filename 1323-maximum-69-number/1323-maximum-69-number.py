class Solution:
    def maximum69Number (self, num: int) -> int:
        l = list(str(num))
        for i,c in enumerate(l):
            if c == '6':
                l[i] = '9'    
                break
        return int(''.join(l))