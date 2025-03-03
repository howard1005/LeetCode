class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l,m,r = [],[],[]

        for n in nums:
            if n < pivot:
                l.append(n)
            elif n == pivot:
                m.append(n)
            else:
                r.append(n)

        return l+m+r