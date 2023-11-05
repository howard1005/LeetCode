class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        mx = arr[0]
        cnt = 0
        for i in range(1,len(arr)):
            if mx < arr[i]:
                mx = arr[i]
                cnt = 1
            else:
                cnt += 1
            if cnt == k:
                return mx
        
        return max(arr)