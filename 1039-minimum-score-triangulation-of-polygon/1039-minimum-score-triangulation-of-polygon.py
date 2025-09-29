class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:

        @cache
        def proc(l):
            if len(l) == 3:
                return l[0]*l[1]*l[2]

            ret = inf

            for i in range(1,len(l)-1):
                a = proc(l[:i+1]) if i>1 else 0
                b = proc(l[i:]) if i<len(l)-2 else 0
                ret = min(ret, a+b+l[0]*l[-1]*l[i])

            return ret
      
        ans = proc(tuple(values))

        return ans