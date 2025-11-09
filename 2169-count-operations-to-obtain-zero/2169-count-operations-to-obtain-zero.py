class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ans = 0

        a,b = num1,num2

        while a and b:
            if a >= b:
                o = a//b
                ans += o
                a -= o*b
            else:
                o = b//a
                ans += o
                b -= o*a
        
        return ans