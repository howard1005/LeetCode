class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        def proc(n):
            if n == 2:
                return -1
            m = n
            cnt = 0
            while m&1:
                cnt += 1
                m >>= 1
            # print(n,cnt)
            return n^(1<<(cnt-1))
        
        ans = [proc(n) for n in nums]

        return ans

