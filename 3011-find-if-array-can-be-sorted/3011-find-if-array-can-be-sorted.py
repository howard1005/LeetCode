class Solution:
    def canSortArray(self, nums: List[int]) -> bool:

        def count_bit(n):
            ret = 0
            while n:
                ret += n&1
                n >>= 1
            return ret

        l = []
        tl = [nums[0]]
        pcnt = count_bit(nums[0])
        for n in nums[1:]:
            cnt = count_bit(n)
            if pcnt == cnt:
                tl.append(n)
            else:
                l.append(tl)
                tl = [n]
                pcnt = cnt
        l.append(tl)

        for i in range(len(l)-1):
            if max(l[i]) > min(l[i+1]):
                return False

        return True
        
            