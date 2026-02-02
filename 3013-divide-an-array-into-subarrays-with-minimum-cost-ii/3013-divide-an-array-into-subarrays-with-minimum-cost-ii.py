from heapq import heappush,heappop

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        ans = inf


        hq1,hq2 = [],[]
        sd1,sd2 = set(),set()
        cum = 0

        def top1():
            while hq1 and hq1[0][1] not in sd1:
                heappop(hq1)
            return hq1[0] if hq1 else (None,None)

        def top2():
            while hq2 and hq2[0][1] not in sd2:
                heappop(hq2)
            return hq2[0] if hq2 else (None,None)

        def add(i):
            nonlocal cum
            n = nums[i]
            v1,i1 = top1()
            if v1:
                v1 = -v1

            if len(sd1) < k-1:
                sd1.add(i)
                heappush(hq1,(-n,i))
                cum += n
            elif v1 and v1>=n:
                sd1.remove(i1)
                heappop(hq1)
                cum -= v1

                sd1.add(i)
                heappush(hq1,(-n,i))
                cum += n

                sd2.add(i1)
                heappush(hq2,(v1,i1))
            elif v1:
                sd2.add(i)
                heappush(hq2,(n,i))
            else:
                sd1.add(i)
                heappush(hq1,(-n,i))
                cum += n

        
        def remove(i):
            nonlocal cum
            n = nums[i]
            if i in sd1:
                sd1.remove(i)
                cum -= n
                if sd2:
                    v2,i2 = top2()
                    sd2.remove(i2)
                    heappop(hq2)
                    sd1.add(i2)
                    heappush(hq1,(-v2,i2))
                    cum += v2
            elif i in sd2:
                sd2.remove(i)

        i,j = 1,1
        while j<len(nums):
            # print("\n",i,j,"="*10)
            # print("before\n",hq1,sd1,"\n",hq2,sd2,"\n",cum)
            if j < k-1:
                add(j)
                j += 1
            elif j <= dist+1:
                add(j)
                j += 1
                ans = min(ans,nums[0]+cum)
            else:
                remove(i)
                i += 1
                add(j)
                j += 1
                ans = min(ans,nums[0]+cum)
            # print("after\n",hq1,sd1,"\n",hq2,sd2,"\n",cum)
                

        return ans