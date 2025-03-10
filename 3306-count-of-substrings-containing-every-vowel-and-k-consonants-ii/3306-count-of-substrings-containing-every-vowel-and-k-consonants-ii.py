class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        ans = 0

        vowel = ('a', 'e', 'i', 'o', 'u')
        
        vd = defaultdict(int)
        cntd = defaultdict(int)
        cntd[0] += 1
        
        cnt = 0
        icnt = 0

        i,j = 0,0
        while j<len(word):
            c = word[j]

            if c in vowel:
                vd[c] += 1
            else:
                cnt += 1

            while i<j and len(vd) == 5:
                cc = word[i]
                if cc in vowel:
                    if vd[cc] > 1:
                        vd[cc] -= 1
                    else:
                        break
                else:
                    icnt += 1
                cntd[icnt] += 1

                i += 1

            # print(i,j,cnt,icnt,vd,cntd)

            if cnt >= k and len(vd) == 5:
                ans += cntd[cnt-k]

            j += 1

        return ans