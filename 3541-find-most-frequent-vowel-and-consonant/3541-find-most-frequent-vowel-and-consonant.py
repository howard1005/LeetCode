class Solution:
    def maxFreqSum(self, s: str) -> int:
        vs = ('a', 'e', 'i', 'o', 'u')

        d = defaultdict(int)

        for c in s:
            d[c] += 1

        vmx = 0
        cmx = 0
        for c,cnt in d.items():
            if c in vs:
                vmx = max(vmx,cnt)
            else:
                cmx = max(cmx,cnt)

        ans = vmx+cmx

        return ans
            

        