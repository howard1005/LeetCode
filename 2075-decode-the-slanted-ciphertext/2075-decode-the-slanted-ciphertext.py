class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)

        def cols():
            ret = 0
            lo,hi = 0,1000000
            while lo<=hi:
                mi = (lo+hi)//2
                if rows*mi >= n:
                    ret = mi
                    hi = mi - 1
                else:
                    lo = mi + 1
            return ret

        r,c = rows,cols()

        ans = ''

        i,j = 0,0
        while i*c+j<n:
            # print(i,j)
            ans += encodedText[i*c+j]
            i+=1
            j+=1
            if i==r:
                i=0
                j=j-r+1
        
        

        return ans.rstrip()