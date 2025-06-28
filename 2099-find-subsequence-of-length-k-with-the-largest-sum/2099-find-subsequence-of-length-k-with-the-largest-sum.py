class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        ans = []
        
        l = [(n,i) for i,n in enumerate(nums)]
        l.sort(reverse=True)
        sl = l[:k]
        sl.sort(key=lambda x: x[1])

        ans = [n for n,_ in sl]

        return ans