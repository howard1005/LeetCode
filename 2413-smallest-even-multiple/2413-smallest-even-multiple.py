class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        def gcd(x,y):
            while y:
                x,y = y,x%y
            return x
        
        def lcm(x,y):
            return x*y // gcd(x,y)
        
        return lcm(n,2)