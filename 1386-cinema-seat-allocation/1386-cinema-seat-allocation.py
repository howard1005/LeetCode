class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        ans = 0
        
        d = defaultdict(set)
        for r,s in reservedSeats:
            d[r].add(s)

        ans += 2*(n-len(d))

        sd1 = {2,3,4,5}
        sd2 = {6,7,8,9}
        sd3 = {4,5,6,7}

        # print(d)

        for r,sd in d.items():
            f = True
            if not sd&sd1:
                ans += 1
                f = False
            if not sd&sd2:
                ans += 1
                f = False
            if f and not sd&sd3:
                ans += 1
                

        return ans