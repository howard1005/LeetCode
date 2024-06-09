class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return abs(k-nums[0])

        ans = inf
        
        l = [[0 for _ in range(31)] for _ in range(len(nums))]
        nl = [0 for _ in range(len(nums))]

        def updateD(n,d,o):
            j = 0
            while n:
                if o == 1:
                    d[j] += n&1
                else:
                    d[j] -= n&1
                j+=1
                n >>= 1
        
        cum = 0
        for i,n in enumerate(nums):
            d = l[i]
            updateD(n,d,1)
            if i:
                for key,v in enumerate(l[i-1]):
                    d[key] += v
            cum |= n
            nl[i] = cum

        @cache
        def sub(j,i): # j - i
            ret = 0
            dj,di = l[j],l[i]
            for key,v in enumerate(di):
                if dj[key] - v:
                    ret |= (1<<key)
            return ret
        
        j = 0
        for i in range(len(l)):
            d = l[i]
            n = nl[i]
            ans = min(ans,abs(k-n))
            while j < i and sub(i,j) > k:
                j += 1
            if j == i:
                continue

            ans = min(ans,abs(k-sub(i,j)))
            if j:
                ans = min(ans,abs(k-sub(i,j-1)))

            # print("i,n,k,j,ans",i,n,k,j,ans)
                
        return ans
                           
                