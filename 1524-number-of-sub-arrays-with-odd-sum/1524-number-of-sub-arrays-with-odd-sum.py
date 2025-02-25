class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        ans = 0

        MOD = 1000000007

        d = defaultdict(int)

        l = [0 for _ in range(len(arr))]
        l[0] = arr[0]
        for i in range(1,len(arr)):
            l[i] = l[i-1] + arr[i]
        
        for i in range(len(arr)):
            if l[i]&1:
                ans = (ans+d[0]+1)%MOD
                d[1] += 1
            else:
                ans = (ans+d[1])%MOD
                d[0] += 1

        return ans
