class Solution:
    def digitSum(self, s: str, k: int) -> str:

        def proc(ts):
            rs = ''
            for i in range(0,len(ts),k):
                sub = ts[i:min(i+k,len(ts))]
                # print('sub',sub)
                tot = sum([int(c) for c in sub])
                # print('tot',tot)
                rs += str(tot)
            return rs

        while len(s) > k:
            # print(s)
            s = proc(s)

        return s