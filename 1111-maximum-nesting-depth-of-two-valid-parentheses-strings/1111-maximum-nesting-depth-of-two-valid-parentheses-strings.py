class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans = []

        a,b = 0,0
        mxa,mxb = 0,0

        for c in seq:
            if c == '(':
                if a > b:
                    b += 1
                    ans.append(1)
                else:
                    a += 1
                    ans.append(0)
            else:
                if a > b:
                    a -= 1
                    ans.append(0)
                else:
                    b -= 1
                    ans.append(1)
            # mxa = max(mxa,a)
            # mxb = max(mxb,b)


        return ans
        
                    
                    