class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        ans = -inf

        pl,ml = [],[]
        z = False

        for n in nums:
            if n>0:
                pl.append(n)
            elif n<0:
                ml.append(n)
            else:
                z = True
        pl.sort()
        ml.sort()
                

        if len(pl)>=3:
            ans = max(ans,pl[-3]*pl[-2]*pl[-1])

        if len(ml)>=1 and len(pl)>=2:
            ans = max(ans,pl[0]*pl[1]*ml[-1])

        if len(ml)>=2 and len(pl)>=1:
            ans = max(ans,pl[-1]*ml[0]*ml[1])

        if len(ml)>=3:
            ans = max(ans,ml[-3]*ml[-2]*ml[-1])

        if z and ans<0:
            ans = 0

        return ans