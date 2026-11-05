class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        ans = 0
        for a in arr1:
            cnt = 0
            for b in arr2:
                if abs(a-b)<=d:
                    cnt += 1
                    break
            if cnt == 0:
                ans += 1
        return ans