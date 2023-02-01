class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        ans = ''
        
        def proc(s1,s2):
            for i in range(len(s1)+1,0,-1):
                if len(s1)%i == 0 and len(s2)%i == 0:
                    t = s1[:i]
                    if s1 == t*(len(s1)//len(t)) and s2 == t*(len(s2)//len(t)):
                        return t
            return ''

        ans = proc(str1,str2) if len(str1) < len(str2) else proc(str2,str1)
        
        return ans

            