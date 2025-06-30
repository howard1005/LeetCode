class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        l = [nums[0]]

        for n in nums[1:]:
            l.append(min(l[-1],n))

        st = []
        
        for i in range(len(nums)-1,-1,-1):
            n = nums[i]
            while st and st[-1] <= l[i]:
                st.pop()
            a = l[i]
            c = st[-1] if st else inf
            if n > c:
                return True
            if c > n:
                st.append(n)
            
        return False
            
                
                
            