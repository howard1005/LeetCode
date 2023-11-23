class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        
        for i,j in zip(l,r):
            sub = nums[i:j+1]
            if len(sub) < 2:
                ans.append(False)
                continue
            sub.sort()
            t = sub[1]-sub[0]
            flag = True
            for k in range(1,len(sub)-1):
                if t != sub[k+1]-sub[k]:
                    flag = False
                    break
            ans.append(flag)
            
        return ans
            