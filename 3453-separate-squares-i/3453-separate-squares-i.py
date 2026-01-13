class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        ans = 1000000000

        a = 0
        for _,_,l in squares:
            a += l*l
        a /= 2

        r = 0.0000001
        
        def valid(h):
            ua,da = 0,0
            for x,y,l in squares:
                if y+l <= h:
                    da += l*l
                elif y >= h:
                    ua += l*l
                else:
                    da += (h-y)*l
                    ua += (y+l-h)*l
            
            # r = 0.000001
            # if ua+da > 1000000:
            #     r = 10
            # elif ua+da > 1000:
            #     r = 0.0001
            # elif ua+da > 100:
            #     r = 0.0001
            # while ua>=1 or da>=1:
            #     ua /= 10
            #     da /= 10
            # print(ua,da,abs(ua-da))

            if abs(a-da) < r:
                return 0
            elif ua>da:
                return 1
            else:
                return -1

        lo,hi = 0,1000000000
        while hi-lo >= 0.000001:
            # print("lo,hi",lo,hi)
            mi = (lo+hi)/2
            f = valid(mi)
            # print("mif",mi,f)
            if f == 0:
                ans = min(ans,mi)
                hi = mi
            elif f == 1:
                lo = mi
            else:
                hi = mi
        ans = mi
                
        return ans

                