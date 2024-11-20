from bisect import bisect_left

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0

        ans = inf
        
        d = defaultdict(int)
        
        l = [[0 for _ in range(len(s))] for _ in range(3)]

        for i,c in enumerate(s):
            tl = []
            for j in range(3):
                l[j][i] += (1 if ord(c)-ord('a') == j else 0) + (l[j][i-1] if i else 0)
                tl.append(l[j][i])
            if min(tl) >= k:
                ans = min(ans,i+1)

        # print(l)
        
        rl = [0,0,0]
        for i in range(len(s)-1,-1,-1):
            c = s[i]
            if c == 'a':
                rl[0] += 1
            if c == 'b':
                rl[1] += 1
            if c == 'c':
                rl[2] += 1

            # print("\n\ni,rl: ", i, rl)

            _anss = [-1,-1,-1]
            for j in range(3):
                if rl[j] < k:
                    jj = bisect_left(l[j],k-rl[j],0,i)
                    # print("j,jj,l[j],rl[j] : ", j, jj, l[j], rl[j])
                    if jj >= i:
                        continue
                    _anss[j] = jj+1+(len(s)-i)
                else:
                    _anss[j] = (len(s)-i)
            # print("_anss: ", _anss)
            
            _ans = -1
            flag = True
            for t in _anss:
                if t == -1:
                    flag = False
                _ans = max(_ans,t)
            
            if _ans != -1 and flag:
                ans = min(ans,_ans)
        
        return ans if ans != inf else -1

