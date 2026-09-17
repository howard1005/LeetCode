class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        ans = inf

        d1 = defaultdict(lambda:-1)
        l1 = [inf for _ in range(len(arr))]
        if arr[0] == target:
            l1[0] = 1
        cum1 = arr[0]
        d1[arr[0]] = 0
        for i in range(1,len(arr)):
            cum1 += arr[i]
            l1[i] = l1[i-1]
            if cum1 == target:
                l1[i] = min(l1[i],i+1)
            else:
                j = d1[cum1-target]
                if j != -1:
                    l1[i] = min(l1[i],i-j)
            d1[cum1] = i

        # print(l1)

        d2 = defaultdict(lambda:-1)
        l2 = [inf for _ in range(len(arr))]
        if arr[-1] == target:
            l2[-1] = 1
        cum2 = arr[-1]
        d2[arr[-1]] = len(arr)-1
        for i in range(len(arr)-2,-1,-1):
            cum2 += arr[i]
            l2[i] = l2[i+1]
            if cum2 == target:
                l2[i] = min(l2[i],len(arr)-i)
            else:
                j = d2[cum2-target]
                if j != -1:
                    l2[i] = min(l2[i],j-i)
            d2[cum2] = i
        
        # print(l2)

        for i in range(len(arr)-1):
            a,b = l1[i],l2[i+1]
            if a!=inf and b!=inf:
                ans = min(ans,a+b)
        

        return ans if ans != inf else -1