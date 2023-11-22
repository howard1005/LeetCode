class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ans = []
        
        d = defaultdict(list)
        
        for i in range(len(nums)-1,-1,-1):
            for j in range(len(nums[i])):
                d[i+j].append(nums[i][j])
        
        for i in range(len(d)):
            ans.extend(d[i])
            
        return ans