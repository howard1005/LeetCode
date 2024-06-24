class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        ans = 0
        
        dq = deque([])

        for i in range(len(nums)):
            while dq and dq[0][1] < i:
                dq.popleft()
            t = nums[i]^(len(dq)&1)
            if t == 0:
                if i+k-1 >= len(nums):
                    return -1
                ans += 1
                dq.append((i,i+k-1))
        
        return ans