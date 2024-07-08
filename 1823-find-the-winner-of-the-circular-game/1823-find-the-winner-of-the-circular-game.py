class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        l = [i+1 for i in range(n)]

        i = 0
        while len(l)>1:
            i = (i+k-1)%len(l)
            del l[i]
            
        return l[0]