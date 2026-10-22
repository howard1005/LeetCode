class Solution:
    def minOperations(self, nums: List[int]) -> int:

        sl = list(sorted(nums))
        if nums == sl:
            return 0

        down,up = set(),set()

        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                up.add((i,i+1))
            else:
                down.add((i,i+1))
        if nums[-1] < nums[0]:
            up.add((len(nums)-1,0))
        else:
            down.add((len(nums)-1,0))
        
            
        if len(down)>1 and len(up)>1:
            return -1

        # print(down,up)

        if len(down) == 1:
            a,b = down.pop()
            return min(b,len(nums)-1-a+2)
        if len(up) == 1:
            a,b = up.pop()
            return min(b+1,len(nums)-1-a+1)

        return -1