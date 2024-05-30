class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans = 0

        for i in range(len(arr)):
            cum = arr[i]
            for k in range(i+1,len(arr)):
                cum ^= arr[k]
                if cum == 0:
                    ans += k-i
        
        return ans