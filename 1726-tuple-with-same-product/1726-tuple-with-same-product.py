class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        ans = 0
        
        d = defaultdict(int)

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                d[nums[i]*nums[j]] += 1

        for cnt in d.values():
            ans += cnt*(cnt-1)*4

        return ans