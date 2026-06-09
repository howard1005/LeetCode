from heapq import heappush,heappop

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        
        exp = 0
        while len(nums)>(1<<exp):
            exp += 1
        tree = [(-1,inf,-1,-inf) for _ in range(1<<(exp+1))]

        def query(us,ue,i=1,s=0,e=(1<<exp)-1):
            if ue < s or e < us:
                return (-1,inf,-1,-inf)
            if us <= s and e <= ue:
                return tree[i]
            
            m = (s+e)//2
            q1 = query(us,ue,i*2,s,m)
            q2 = query(us,ue,i*2+1,m+1,e)
            tl = [None,None,None,None]
            if q1[1] > q2[1]:
                tl[0] = q2[0]
                tl[1] = q2[1]
            else:
                tl[0] = q1[0]
                tl[1] = q1[1]
            if q1[3] < q2[3]:
                tl[2] = q2[2]
                tl[3] = q2[3]
            else:
                tl[2] = q1[2]
                tl[3] = q1[3]

            return tuple(tl)

        def update(us,ue,uv,i=1,s=0,e=(1<<exp)-1):
            if ue < s or e < us:
                return 
            if us <= s and e <= ue:
                tree[i] = (us,uv,us,uv)
                return
            
            m = (s+e)//2
            update(us,ue,uv,i*2,s,m)
            update(us,ue,uv,i*2+1,m+1,e)

            q1 = tree[i*2]
            q2 = tree[i*2+1]
            tl = [None,None,None,None]
            if q1[1] > q2[1]:
                tl[0] = q2[0]
                tl[1] = q2[1]
            else:
                tl[0] = q1[0]
                tl[1] = q1[1]
            if q1[3] < q2[3]:
                tl[2] = q2[2]
                tl[3] = q2[3]
            else:
                tl[2] = q1[2]
                tl[3] = q1[3]

            tree[i] = tuple(tl)

        for i,n in enumerate(nums):
            update(i,i,n)

        # print(tree)

        ans = 0

        vis = set()

        t = query(0,len(nums)-1)
        # print("t", t)
        vis.add((0,len(nums)-1))
        hq = [(-(t[3]-t[1]),0,len(nums)-1,*t)]
        
        # print(hq)
        while hq:
            diff,a,b,mni,mn,mxi,mx = heappop(hq)
            # print("hq: ",diff,a,b,mni,mn,mxi,mx)
            i,j = (mni,mxi) if mni<=mxi else (mxi,mni)
            cnt = (i-a+1)*(b-j+1)
            # print('cnt',cnt)
            if k > cnt:
                k -= cnt
                ans += -diff*cnt
            else:
                ans += -diff*k
                k = 0
                break
            # print('ans',ans)
            if (a,j-1) not in vis:
                vis.add((a,j-1))
                q1 = query(a,j-1)
                heappush(hq,(-(q1[3]-q1[1]),a,j-1,*q1))
            if (i+1,b) not in vis:
                vis.add((i+1,b))
                q2 = query(i+1,b)
                heappush(hq,(-(q2[3]-q2[1]),i+1,b,*q2))

        return ans


        
            
            
            
        