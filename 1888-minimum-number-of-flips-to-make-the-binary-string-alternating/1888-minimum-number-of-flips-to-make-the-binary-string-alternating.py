class Solution:
    def minFlips(self, s: str) -> int:
        ans = -1

        e0,e1 = 0,0
        o0,o1 = 0,0
        for i,c in enumerate(s):
            if i%2 == 0 and c == '0':
                e0 += 1
            if i%2 == 0 and c == '1':
                e1 += 1
            if i%2 == 1 and c == '0':
                o0 += 1
            if i%2 == 1 and c == '1':
                o1 += 1
        # print(e0,e1,o0,o1)
        ans = min(e0+o1,e1+o0)

        if len(s)%2 == 1:
            ae0,ae1 = 0,0
            ao0,ao1 = 0,0
            for i,c in enumerate(s):
                if i%2 == 0 and c == '0':
                    ae0 += 1
                if i%2 == 0 and c == '1':
                    ae1 += 1
                if i%2 == 1 and c == '0':
                    ao0 += 1
                if i%2 == 1 and c == '1':
                    ao1 += 1
                _ans = min((e0-ae0+ao0)+(o1+ae1-ao1),(e1-ae1+ao1)+(o0+ae0-ao0))
                ans = min(ans,_ans)

            

        return ans
            