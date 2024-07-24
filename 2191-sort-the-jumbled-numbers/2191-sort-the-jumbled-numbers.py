class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        
        def doMapping(n):
            if n == 0:
                return mapping[0]
            ret = 0
            i = 1
            while n:
                ret += i*mapping[n%10]
                n //= 10
                i *= 10
            return ret

        l = [(doMapping(n),i) for i,n in enumerate(nums)]
        l.sort()

        return [nums[i] for _,i in l]
        

        