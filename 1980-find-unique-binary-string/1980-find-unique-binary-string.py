class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def bin2num(s):
            ret = 0
            for c in s:
                ret = ret*2 + int(c)
            return ret
        
        def num2bin(n):
            ret = ''
            while n:
                ret = str(n&1) + ret
                n >>= 1
            pad = len(nums[0]) - len(ret)
            if pad > 0:
                ret = '0'*pad + ret
            return ret
        
        d = set()
        for s in nums:
            d.add(bin2num(s))
        
        for n in range(1<<len(nums)):
            if n not in d:
                return num2bin(n)