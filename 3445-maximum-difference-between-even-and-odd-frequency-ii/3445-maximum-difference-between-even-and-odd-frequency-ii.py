class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        ans = -inf

        def proc(a,b):
            # print("---",a,b)
            nonlocal ans
            d = defaultdict(lambda:inf) # (짝0,홀1):min(a-b)

            dq = deque()

            acnt,bcnt = 0,0

            for i in range(len(s)):
                c = s[i]
                n = int(c)

                if n == a:
                    acnt += 1
                if n == b:
                    bcnt += 1

                while len(dq) >= k:
                    _t,_diff,_acnt,_bcnt = dq[0]
                    if acnt == _acnt or bcnt == _bcnt:
                        break
                    # print("write",_t,_diff)
                    d[_t] = min(d[_t],_diff)
                    dq.popleft()

                t = (acnt&1,bcnt&1)

                diff = acnt-bcnt

                # print(i,acnt,bcnt,diff,d)

                if acnt and bcnt and i >= k-1:
                    if t == (1,0):
                        # print("raw match",t,diff)
                        ans = max(ans,diff)

                    if t == (0,0) and (1,0) in d:
                        # print("match",t,diff,diff-d[(1,0)])
                        ans = max(ans,diff-d[(1,0)])
                    if t == (0,1) and (1,1) in d:
                        # print("match",t,diff,diff-d[(1,1)])
                        ans = max(ans,diff-d[(1,1)])
                    if t == (1,0) and (0,0) in d:
                        # print("match",t,diff,diff-d[(0,0)])
                        ans = max(ans,diff-d[(0,0)])
                    if t == (1,1) and (0,1) in d:
                        # print("match",t,diff,diff-d[(0,1)])
                        ans = max(ans,diff-d[(0,1)])

                dq.append((t,diff,acnt,bcnt))
                # print("update dq",dq)

        for a in range(5):
            for b in range(5):
                if a == b:
                    continue
                proc(a,b)
                

        return ans