class Solution:
    d = {}
    def findKthBit(self, n: int, k: int) -> str:
        ans = ''

        def invert(s):
            rets = ''
            for c in s:
                if c == '0':
                    rets += '1'
                else:
                    rets += '0'
            return rets

        def reverse(s):
            return s[::-1]

        

        d = self.d

        if not d:
            s = '0'
            d[1] = s
            for i in range(2,21):
                s = s + "1" + reverse(invert(s))
                d[i] = s

        # print(d)

        ans = d[n][k-1]

        return ans