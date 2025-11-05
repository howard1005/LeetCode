from heapq import heappush,heappop

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        i,j = 0,0

        d = defaultdict(int)
        while j<k:
            d[nums[j]] += 1
            j += 1
        
        rd = defaultdict(int)
        rhq = []
        for v,cnt in d.items():
            rd[v] = cnt
            heappush(rhq,(-cnt,-v))

        xcum = 0
        xd = defaultdict(int)
        xhq = []
        while rhq and len(xd)<x:
            cnt,v = heappop(rhq)
            cnt,v = -cnt,-v
            xcum += cnt*v
            xd[v] = cnt
            del rd[v]
            heappush(xhq,(cnt,v))

        def top(hq,dd):
            while hq and (abs(hq[0][1]) not in dd or dd[abs(hq[0][1])] != abs(hq[0][0])):
                heappop(hq)
            return hq[0] if hq else None

        def pop(hq,dd):
            top(hq,dd)
            return heappop(hq) if hq else None

        def update_x(v,op):
            nonlocal xcum
            xcum += op*v
            xd[v] += op
            if xd[v] == 0:
                del xd[v]
            else:
                heappush(xhq,(xd[v],v))

        ans = []

        while i<len(nums)-k+1:
            # top(xhq,xd),top(rhq,rd)
            # print("\n===============================================")
            # print(f"{d}\n{xd}\n{xhq}\n{rd}\n{rhq}")
            

            ans.append(xcum)
            
            a = nums[i]
            d[a] -= 1
            if a in xd:
                update_x(a,-1)
            else:
                rd[a] -= 1
                if rd[a] == 0:
                    del rd[a]
                else:
                    heappush(rhq,(-rd[a],-a))
            
            # print(f"중간1 xd {xd}, {xhq}")
            # print(f"중간1 rd {rd}, {rhq}")

            if j<len(nums):
                b = nums[j]
                d[b] += 1
                if b in xd:
                    update_x(b,1)
                else:
                    rd[b] += 1
                    heappush(rhq,(-rd[b],-b))

            # print(f"중간2 xd {xd}, {xhq}")
            # print(f"중간2 rd {rd}, {rhq}")


            t = top(rhq,rd)
            if t:
                t = (abs(t[0]),abs(t[1]))
                xt = top(xhq,xd)
                if len(xd) < x:
                    # print(f"x 부족 : 채움 {t}")
                    cnt,v = t
                    update_x(v,cnt)
                    del rd[v]
                    top(rhq,rd)
                    
                elif xt < t:
                    # print(f"교환 : {xt}, {t}")
                    update_x(xt[1],-xt[0])
                    update_x(t[1],t[0])
                    
                    del rd[t[1]]
                    top(rhq,rd)
                    rd[xt[1]] = xt[0]
                    heappush(rhq,(-xt[0],-xt[1]))
                    # print(f"교환 rd : {rd} {rhq}")
                    

            j += 1
            i += 1

        return ans