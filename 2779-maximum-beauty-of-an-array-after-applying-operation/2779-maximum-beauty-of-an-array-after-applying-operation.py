class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        ans = 0

        nums.sort()

        dq = deque()
        for n in nums:
            while dq and dq[0] < n-k:
                dq.popleft()
            dq.append(n+k)
            ans = max(ans,len(dq))

        return ans