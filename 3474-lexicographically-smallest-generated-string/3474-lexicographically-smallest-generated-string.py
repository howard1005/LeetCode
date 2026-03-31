class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        ansl = []

        n,m = len(str1),len(str2)

        pi = [0 for _ in range(m)]
        
        j = 0
        for i in range(1,len(pi)):
            while j>0 and str2[i] != str2[j]:
                j = pi[j-1]
            if str2[i] == str2[j]:
                j += 1
                pi[i] = j

        # print(pi)

        ansl = ['' for _ in range(n+m-1)]

        td = set()

        for i,c in enumerate(str1):
            if c == 'T':
                td.add(i)
                for j in range(i,i+m):
                    if ansl[j] and ansl[j] != str2[j-i]:
                        return ''
                    ansl[j] = str2[j-i]

        i,j = 0,0
        while i < len(ansl):
            # print(i,j)
            c = ansl[i] if ansl[i] else 'a'
            while j>0 and c != str2[j]:
                j = pi[j-1]
            if c == str2[j]:
                j += 1
            if j == m:
                k = i-m+1
                if k not in td:
                    ii = i
                    while ii >= k and ansl[ii]:
                        ii -= 1
                        j -= 1
                    if ii >= k:
                        # print('convert', i,j)
                        ansl[ii] = 'b'
                        i = ii
                        j -= 1
                        continue
                    else:
                        # print('i,ii',i,ii,ansl)
                        return ''
                j = pi[m-1]

            i += 1

        # print(ansl)

        ans = ''.join([c if c else 'a' for c in ansl ])

        return ans