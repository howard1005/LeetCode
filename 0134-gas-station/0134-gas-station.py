class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        l = [g-c for g,c in zip(gas,cost)]*2
        #print(l)
        s,e,cum = 0,0,l[0]
        while s<len(gas):
            #print(s,e,cum)
            if cum >= 0:
                if e-s == len(gas)-1:
                    return s
                e += 1
                cum += l[e]
            else:
                cum -= l[s]
                s += 1
                if s>e:
                    e = s
                    cum = l[e]

            
        return -1
        