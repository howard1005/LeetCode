class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        fl = [False for _ in range(len(arr))]
        bl = [False for _ in range(len(arr))]
        
        fl[0] = True
        for i in range(1,len(arr)):
            if arr[i-1] <= arr[i]:
                fl[i] = True
            else:
                break
        
        bl[-1] = True
        for i in range(len(arr)-2,-1,-1):
            if arr[i] <= arr[i+1]:
                bl[i] = True
            else:
                break

        # print(fl,bl)

        def valid(t):
            # print(f"t:{t}")
            if t<len(bl) and bl[t]:
                # print(f"bl[t]:{bl[t]}")
                return True
            if -t-1 >= -len(fl) and fl[-t-1]:
                # print(f"fl[-t-1]:{fl[-t-1]}")
                return True
            for i in range(len(arr)):
                j = i+t-1
                if i and j<len(arr)-1 and arr[i-1]<=arr[j+1] and fl[i-1] and bl[j+1]:
                    return True
            return False

        ans = len(arr)-1

        lo,hi = 0,len(arr)
        while lo<=hi:
            mi = (lo+hi)//2
            if valid(mi):
                ans = min(ans,mi)
                hi = mi - 1
            else:
                lo = mi + 1

        return ans