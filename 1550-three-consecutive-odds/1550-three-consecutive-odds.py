class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:

        def valid(i):
            for j in range(i,i+3):
                if arr[j]%2==0:
                    return False
            return True

        for i in range(len(arr)-2):
            if valid(i):
                return True
        
        return False

                    