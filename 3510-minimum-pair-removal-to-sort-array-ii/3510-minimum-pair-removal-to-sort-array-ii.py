from heapq import heappush,heappop

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ans = 0
        
        pars = [i for i in range(len(nums))]

        def find_par(i):
            tl = []
            while pars[i] != i:
                tl.append(i)
                i = pars[i]
            for j in tl:
                pars[j] = i
            return i

        def union(i,j):
            pi,pj = find_par(i),find_par(j)
            pi,pj = min(pi,pj),max(pi,pj)
            pars[pj] = pi
            return pi

        cd = set()
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                cd.add(i)

        hq = [] # (sum,i,j,time)
        for i in range(len(nums)-1):
            p = nums[i]+nums[i+1]
            heappush(hq,(p,i,i+1,0))

        lastd = {}
        for i in range(len(nums)):
            lastd[i] = i

        td = defaultdict(int)
        time = 0
        while cd:
            # print("prev hq",hq)
            while hq:
                p,i,j,t = hq[0]
                if td[(i,j)] != t:
                    heappop(hq)
                    continue
                else:
                    break
            # print("next hq",hq)
            if not hq:
                # print("not hq")
                break

            time += 1
            # print(time,nums,hq,cd,pars,td)
            p,i,j,t = heappop(hq)
            pi = union(i,j)
            nums[j] = None
            nums[pi] = p
            lastd[pi] = max(lastd[pi],i,j,lastd[j])
            td[(i,j)] = time

            if i in cd:
                cd.remove(i)
            if j in cd:
                cd.remove(j)

            if pi-1>=0:
                ppi = find_par(pi-1)
                # print("ppi",ppi,nums[ppi])
                if nums[ppi] > p:
                    cd.add(ppi)
                elif ppi in cd:
                    cd.remove(ppi)
                td[(ppi,pi)] = time
                heappush(hq,(nums[ppi]+p,ppi,pi,time))
            
            npi = lastd[pi]+1
            if npi < len(nums) and nums[npi] != None:
                if p > nums[npi]:
                    cd.add(pi)
                elif pi in cd:
                    cd.remove(pi)
                td[(i,npi)] = time
                td[(j,npi)] = time
                heappush(hq,(p+nums[npi],pi,npi,time))
            

        ans = time

        return ans
        
