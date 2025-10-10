class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        ans = -inf

        @cache
        def proc(i):
            if i >= len(energy):
                return 0
            return proc(i+k) + energy[i]

        for i in range(len(energy)):
            ans = max(ans,proc(i))


        return ans
                