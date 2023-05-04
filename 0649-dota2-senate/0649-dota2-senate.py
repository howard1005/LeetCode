class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        flag = 0
        
        rcnt = list(senate).count('R')
        dcnt = list(senate).count('D')
        
        l = [1 for _ in range(len(senate))]
        
        while 1:
            for i in range(len(senate)) :
                c,life = senate[i],l[i]
                if life:
                    if c == 'R':
                        if dcnt == 0:
                            return "Radiant"
                        if flag < 0:
                            rcnt -= 1
                            l[i] = 0
                        flag += 1
                    else:
                        if rcnt == 0:
                            return "Dire"
                        if flag > 0:
                            dcnt -= 1
                            l[i] = 0
                        flag -= 1