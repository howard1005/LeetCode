class LL:
    def __init__(self,v,p=None,n=None):
        self.v = v
        self.p = p
        self.n = n

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:       
        st = []
        
        i = 0
        while i < len(asteroids):
            n = asteroids[i]
            
            if st and st[-1] > 0 and n < 0:
                if abs(st[-1]) < abs(n):
                    st.pop()
                elif abs(st[-1]) > abs(n):
                    i += 1
                else:
                    st.pop()
                    i += 1
            else:
                st.append(n)
                i += 1

        return st