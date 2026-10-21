class Solution:
    def minOperations(self, s: str) -> int:

        l = list(s)
        sl = list(sorted(l))
        if l == sl:
            return 0

        if len(l) == 2:
            return -1
        
        if l[0] == sl[0] or l[-1] == sl[-1]:
            return 1

        mn,mx = min(l),max(l)
        mnc,mxc = l.count(mn),l.count(mx)
        if mn == l[-1] and mx == l[0] and mnc == 1 and mxc == 1:
            return 3

        return 2