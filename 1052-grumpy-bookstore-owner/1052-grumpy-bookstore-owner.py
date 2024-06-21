class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        ans = 0
        
        cum = 0
        l = []
        for c,g in zip(customers,grumpy):
            if g:
                l.append(c)
            else:
                cum += c
                l.append(0)

        u = 0
        for c in l[:minutes]:
            u += c

        i,j = 0,minutes-1
        while j < len(l):
            ans = max(ans,cum+u)
            u -= l[i]
            i += 1
            j += 1
            if j < len(l):
                u += l[j]
        
        return ans
