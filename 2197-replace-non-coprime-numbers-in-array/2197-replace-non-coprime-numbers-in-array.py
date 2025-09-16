class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return a * b // gcd(a, b)

        st = []

        for n in nums:
            while st and gcd(st[-1],n)>1:
                n = lcm(n,st.pop())
            st.append(n)

        ans = st

        return ans

        
            
            


                    