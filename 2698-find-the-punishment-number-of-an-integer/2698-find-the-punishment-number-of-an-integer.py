class Solution:
    ansd = {}
    def punishmentNumber(self, n: int) -> int:

        if not self.ansd:  
            d = defaultdict(set)

            def pun(i,s,tl,cum):
                if i == len(s):
                    if tl:
                        cum += int(''.join(tl))
                    d[s].add(cum)
                    return
                pun(i+1,s,tl+[s[i]],cum)
                cum += int(''.join(tl+[s[i]]))
                pun(i+1,s,[],cum)

            cum = 0
            for i in range(1,1001):
                sq = i*i
                s = str(sq)
                pun(0,s,[],0)
                if i in d[s]:
                    cum += sq
                self.ansd[i] = cum

        return self.ansd[n]

            
                
            