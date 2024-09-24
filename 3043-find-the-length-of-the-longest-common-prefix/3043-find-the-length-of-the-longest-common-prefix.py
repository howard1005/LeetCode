class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        ans = 0
        
        sd = set()
        for n in arr1:
            while n:
                sd.add(n)
                n//=10
        
        for n in arr2:
            while n:
                if n in sd:
                    ans = max(ans,len(str(n)))
                    break
                n//=10

        return ans