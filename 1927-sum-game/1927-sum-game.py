class Solution:
    def sumGame(self, num: str) -> bool:
        size = len(num)

        v1,v2 = 0,0
        cnt1,cnt2 = 0,0
        for i in range(size):
            if num[i] == '?':
                if i<size//2:
                    cnt1 += 1
                else:
                    cnt2 += 1
            else:
                if i<size//2:
                    v1 += int(num[i])
                else:
                    v2 += int(num[i])

        if (cnt1+cnt2)&1:
            return True

        if cnt1+cnt2 == 0:
            return v1 != v2

        # print(v1,cnt1,v2,cnt2)
        
        return 2 * (v1 - v2) != 9 * (cnt2 - cnt1)

        
        

        

                