class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        ans = 0

        ocnt,ecnt = 0,0
        for n in nums:
            if n%2:
                ocnt += 1
            else:
                ecnt += 1
        
        ans = max(ocnt,ecnt)

        olen,elen = 0,0
        for n in nums:
            if n%2:
                olen = max(olen,elen+1)
            else:
                elen = max(elen,olen+1)

        ans = max(ans,max(olen,elen))

        return ans