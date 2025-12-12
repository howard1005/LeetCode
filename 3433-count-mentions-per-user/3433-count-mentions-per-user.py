class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        ans = [0 for _ in range(numberOfUsers)]
        
        ofd = {}

        events.sort(key=lambda x:(int(x[1]),-ord(x[0][0])))

        for ty,t,ms in events:
            t = int(t)
            for k,v in list(ofd.items()):
                if v<=t:
                    del ofd[k]

            if ty == 'MESSAGE':
                if ms == 'ALL':
                    for i in range(numberOfUsers):
                        ans[i] += 1
                elif ms == 'HERE':
                    for i in range(numberOfUsers):
                        if i not in ofd:
                            ans[i] += 1
                else:
                    ids = [int(s[2:]) for s in ms.split(' ')]
                    for i in ids:
                        ans[i] += 1
            else:
                ofd[int(ms)] = t+60

        return ans
            