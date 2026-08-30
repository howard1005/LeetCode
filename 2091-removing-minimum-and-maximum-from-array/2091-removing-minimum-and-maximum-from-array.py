class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mn,mni = inf,-1
        mx,mxi = -inf,-1

        for i,n in enumerate(nums):
            if mn > n:
                mn = n
                mni = i
            if mx < n:
                mx = n
                mxi = i

        i,j = min(mni,mxi),max(mni,mxi)

        ans = min(j+1,len(nums)-i,i+1+len(nums)-j)

        return ans