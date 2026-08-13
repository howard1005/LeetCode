from sortedcontainers import SortedList
from heapq import heappush,heappop

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        ans = []

        sl = SortedList()

        id_cnt = 0
        id_sd = set()
        hq = []

        def req_id():
            nonlocal id_cnt
            ret = id_cnt
            id_cnt += 1
            return ret

        pc = ''
        pi = 0
        for i,c in enumerate(s):
            if pc == c:
                pass
            else:
                if pc:
                    idx = req_id()
                    id_sd.add(idx)
                    heappush(hq,(-(i-pi),idx))
                    sl.add(((pi,i-1),pc,idx))
                pi = i
                pc = c
        idx = req_id()
        id_sd.add(idx)
        heappush(hq,(-(len(s)-pi),idx))
        sl.add(((pi,len(s)-1),pc,idx))

        # print(sl)
        
        for qc,qi in zip(queryCharacters,queryIndices):
            pos = sl.bisect_right(((qi, float('inf')),)) - 1
            (l, r), old_c, old_id = sl[pos]

            if old_c != qc:
                sl.pop(pos)
                id_sd.discard(old_id)

                new_l = new_r = qi

                # 왼쪽에 남는 기존 구간
                if l < qi:
                    idx = req_id()
                    id_sd.add(idx)
                    sl.add(((l, qi - 1), old_c, idx))
                    heappush(hq, (-(qi - l), idx))
                elif pos > 0:
                    (ll, lr), lc, lid = sl[pos - 1]
                    if lr == qi - 1 and lc == qc:
                        sl.pop(pos - 1)
                        id_sd.discard(lid)
                        new_l = ll
                        pos -= 1

                # 오른쪽에 남는 기존 구간
                if qi < r:
                    idx = req_id()
                    id_sd.add(idx)
                    sl.add(((qi + 1, r), old_c, idx))
                    heappush(hq, (-(r - qi), idx))
                else:
                    right_pos = pos + (1 if l < qi else 0)

                    if right_pos < len(sl):
                        (rl, rr), rc, rid = sl[right_pos]
                        if rl == qi + 1 and rc == qc:
                            sl.pop(right_pos)
                            id_sd.discard(rid)
                            new_r = rr

                idx = req_id()
                id_sd.add(idx)
                sl.add(((new_l, new_r), qc, idx))
                heappush(hq, (-(new_r - new_l + 1), idx))

            while hq and hq[0][1] not in id_sd:
                heappop(hq)

            ans.append(-hq[0][0])



        return ans