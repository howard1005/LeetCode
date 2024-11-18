class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        ansl = [0 for i in range(len(code))]

        if k == 0:
            return ansl

        size = len(code)

        def lsum(a,b):
            ret = 0
            for i in range(a,b+1):
                j = (i+size)%size
                ret += code[j]
            return ret

        for i in range(size):
            if k > 0:
                a = i+1
                b = i+k
                ansl[i] = lsum(a,b)
            else:
                a = i+k
                b = i-1
                ansl[i] = lsum(a,b)

        return ansl