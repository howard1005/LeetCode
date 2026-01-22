class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ans = 0

        def valid(l):
            for i in range(len(l)-1):
                if l[i]>l[i+1]:
                    return False
            return True

        l = nums[:]
        while valid(l) == False:
            ans += 1
            mn = inf
            mni = -1
            for i in range(len(l)-1):
                t = l[i]+l[i+1]
                if t<mn:
                    mn = t
                    mni = i
            if mni != -1:
                l[mni] = mn
                del l[mni+1]    
            
        return ans