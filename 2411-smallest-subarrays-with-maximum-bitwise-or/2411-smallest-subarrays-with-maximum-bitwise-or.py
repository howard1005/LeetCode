class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        ans = [0 for _ in range(len(nums))]

        def bitd(n):
            retd = defaultdict(int)
            i = 0
            while n:
                if n&1:
                    retd[i] = 1
                i += 1
                n >>= 1
            return retd

        def addd(d1,d2):
            retd = d1.copy()
            for i in range(32):
                retd[i] += d2[i]
            return retd

        def subd(d1,d2):
            retd = d1.copy()
            for i in range(32):
                retd[i] -= d2[i]
            return retd

        def availableSub(d1,d2):
            # print(f"availableSub {d1} {d2}")
            for i in range(32):
                if d1[i] != 0 and d1[i] <= d2[i]:
                    return False
            return True
                    

        dl = [bitd(n) for n in nums]

        d = defaultdict(int)
        i,j = len(nums)-1,len(nums)-1

        while i>=0:
            d = addd(d,dl[i])
            while i<j and availableSub(d,dl[j]):
                d = subd(d,dl[j])
                j -= 1
            ans[i] = j-i+1
            i -= 1
        

        return ans
        