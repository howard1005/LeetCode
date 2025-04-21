class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        l = [0]
        for diff in differences:
            l.append(l[-1]+diff)

        mn,mx = min(l),max(l)
        lu = upper-lower
        nx = mx-mn
        if lu < nx:
            return 0

        return lu-nx+1