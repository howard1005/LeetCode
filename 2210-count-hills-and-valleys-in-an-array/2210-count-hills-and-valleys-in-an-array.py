class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        ans = 0

        l = []

        for n in nums:
            if not l:
                l.append(n)
            else:
                if l[-1] != n:
                    l.append(n)
        
        for i in range(1,len(l)-1):
            if l[i-1] > l[i] and l[i] < l[i+1]:
                ans += 1
            if l[i-1] < l[i] and l[i] > l[i+1]:
                ans += 1
            

        return ans