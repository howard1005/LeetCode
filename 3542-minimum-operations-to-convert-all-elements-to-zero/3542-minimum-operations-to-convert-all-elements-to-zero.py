class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0

        st = []

        for n in nums:
            while st and st[-1] > n:
                st.pop()
                ans += 1
            if st and st[-1] == n:
                pass
            elif n == 0:
                pass
            else:
                st.append(n)
        
        ans += len(st)

        return ans