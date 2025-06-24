class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans = []

        sd = set()

        for i,n in enumerate(nums):
            if n == key:
                for j in range(max(0,i-k),min(len(nums),i+k+1)):
                    sd.add(j)

        ans = list(sd)
        ans.sort()

        return ans